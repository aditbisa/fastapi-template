import pytest
from sqlalchemy.orm import Session

from app.models.users import UserModel
from app.schemas.authentications import UserInfo
from app.services.authentications import (
    authenticate_user,
    create_access_token,
    verify_access_token,
)


def test_authenticate_user_success(session: Session, user_entry: UserModel):
    """
    Test authenticate_user function from services.
    """
    user = authenticate_user(session, "username", "password")
    assert user == user_entry


@pytest.mark.parametrize(
    "username, password",
    [
        ("user-name", "password"),
        ("username", "pass-word"),
        ("aditya", "secret"),
    ],
)
def test_authenticate_user_failed(session: Session, username: str, password: str):
    """
    Test authenticate_user function from services.
    """
    assert authenticate_user(session, username, password) is False


def test_create_access_token_and_verify_access_token(user_entry: UserModel):
    """
    Test create_access_token and verify_access_token function from services.
    """
    access_token = create_access_token(user_entry)
    user_info = verify_access_token(access_token)
    expected_user_info = UserInfo(id=user_entry.id, short_name=user_entry.short_name)
    assert user_info == expected_user_info


@pytest.mark.parametrize(
    "access_token",
    [
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia"
        "WF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    ],
)
def test_verify_access_token(access_token: str):
    """
    Test verify_access_token function from services.
    """
    assert verify_access_token(access_token) is False

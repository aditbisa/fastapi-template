from sqlalchemy.orm import Session

from app.models import UserModel


def test_user_model(session: Session):
    """
    Test UserModel.
    """
    user = UserModel(
        username="user-name",
        password="user-password",
    )
    session.add(user)
    session.commit()

    created_user = session.query(UserModel).one()
    assert created_user.username == "user-name"
    assert created_user.password != "user-password"
    assert created_user.verify_password("user-password") == 1

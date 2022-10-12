import json
from unittest.mock import mock_open, patch

import pytest

from app.configs import get_user_roles_config
from app.schemas.authentications import UserInfo
from app.services.authorizations import get_user_role


@pytest.fixture
def mock_user_roles_config():
    """
    Mock user roles config.
    """
    config = {
        "roles": [
            {
                "id": "role1",
                "name": "Role #1",
                "description": "Role number one.",
                "permissions": ["action1", "action2"],
            },
            {
                "id": "role2",
                "name": "Role #2",
                "description": "Role number two.",
                "permissions": ["action1", "action3"],
            },
        ],
    }
    config_json = json.dumps(config)
    patcher = patch("pathlib.Path.open", mock_open(read_data=config_json))
    get_user_roles_config.cache_clear()
    patcher.start()
    yield
    patcher.stop()
    get_user_roles_config.cache_clear()


@pytest.mark.parametrize(
    "role_id, can_do_action, cannot_do_action",
    [
        ("role1", "action1", "action3"),
        ("role2", "action3", "action2"),
    ],
)
def test_get_user_role(mock_user_roles_config, role_id, can_do_action, cannot_do_action):
    """
    Test get_user_role function from services as well as UserInfo.can_do method.
    """
    user_role: UserInfo = get_user_role(role_id)  # typing here just to show we test UserInfo too
    assert user_role.can_do(can_do_action) is True
    assert user_role.can_do(cannot_do_action) is False

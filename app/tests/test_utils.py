import pytest

from app.utils import snake_to_camel


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ("first_second", "firstSecond"),
        ("first_second_third", "firstSecondThird"),
        ("Single", "single"),
    ],
)
def test_snake_to_camel(input: str, expected_result: str):
    result = snake_to_camel(input)
    assert result == expected_result

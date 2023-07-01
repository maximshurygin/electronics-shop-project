import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def keyboard():
    return Keyboard('Test', 1000, 10)


def test_change_lang(keyboard):
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang().change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'

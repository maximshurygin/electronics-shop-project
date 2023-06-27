import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("Test1", 1, 2, 3)


def test_add(phone):
    phone2 = Phone("Test2", 10, 20, 30)
    assert phone + phone2 == 22


def test_str(phone):
    assert str(phone) == "Test1"


def test_repr(phone):
    assert repr(phone) == "Phone('Test1', 1, 2, 3)"


def test_number_of_sim(phone):
    phone.number_of_sim = 5

    assert phone.number_of_sim == 5

    with pytest.raises(TypeError):
        phone.number_of_sim = 0

    with pytest.raises(TypeError):
        phone.number_of_sim = 1.2

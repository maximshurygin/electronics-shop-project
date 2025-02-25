"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Test", 10, 5)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50


def test_apply_discount(item):
    assert item.price == 10
    item.apply_discount()
    assert item.price == 10 * Item.pay_rate


def test_string_to_number(item):
    assert item.string_to_number('7.7') == 7


def test_instantiate_from_csv(item):
    item.instantiate_from_csv()
    assert len(item.all)


def test_repr(item):
    assert repr(item) == "Item('Test', 10, 5)"


def test_str(item):
    assert str(item) == 'Test'


def test_add(item):
    item2 = Item("Test2", 1, 2)
    assert item + item2 == 7


def test_name(item):
    item.name = 'test_item'
    assert item.name == 'test_item'

    item.name = 'first_test_item'
    assert item.name == 'first_test'

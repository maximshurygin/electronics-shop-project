"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Test", 10, 5)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50

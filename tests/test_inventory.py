import pytest

from src.inventory import get_low_stock_items


def test_get_low_stock_items_returns_correct_items():
    items = [
        {"name": "Clean Code", "stock": 2},
        {"name": "Refactoring", "stock": 10},
        {"name": "Database Systems", "stock": 0},
    ]
    result = get_low_stock_items(items, threshold=5)
    assert len(result) == 2
    assert result[0]["name"] == "Clean Code"
    assert result[1]["name"] == "Database Systems"

def test_get_low_stock_items_empty_list():
    assert get_low_stock_items([], threshold=5) == []

def test_get_low_stock_items_invalid_threshold_raises_error():
    items = [{"name": "Book A", "stock": 5}]
    with pytest.raises(ValueError):
        get_low_stock_items(items, threshold=-1)
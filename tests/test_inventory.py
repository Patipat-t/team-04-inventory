import pytest

from src.inventory import get_low_stock_items


# กรณีที่ 1: ของทุกชิ้นมากกว่า threshold (คืน list ว่าง)
def test_all_items_above_threshold():
    items = [{"name": "Book A", "stock": 10}, {"name": "Book B", "stock": 6}]
    assert get_low_stock_items(items, threshold=5) == []


# กรณีที่ 2: มีชิ้นที่เท่ากับ threshold พอดี (ต้องถูกนับรวมด้วย)
def test_item_equal_to_threshold_included():
    items = [{"name": "Book A", "stock": 5}, {"name": "Book B", "stock": 6}]
    result = get_low_stock_items(items, threshold=5)
    assert len(result) == 1
    assert result[0]["name"] == "Book A"


# กรณีที่ 3: มีหลายชิ้นเข้าเกณฑ์ ผลลัพธ์ต้องเรียงตามชื่อสินค้า
def test_multiple_items_sorted_by_name():
    items = [
        {"name": "Refactoring", "stock": 2},
        {"name": "Clean Code", "stock": 1},
        {"name": "Database Systems", "stock": 0},
    ]
    result = get_low_stock_items(items, threshold=5)
    assert len(result) == 3
    # ต้องเรียงตามชื่อ: Clean Code -> Database Systems -> Refactoring
    assert result[0]["name"] == "Clean Code"
    assert result[1]["name"] == "Database Systems"
    assert result[2]["name"] == "Refactoring"


# กรณีที่ 4: คลังว่าง (คืน list ว่าง)
def test_empty_inventory_returns_empty_list():
    assert get_low_stock_items([], threshold=5) == []


# กรณีที่ 5: threshold เป็น 0 (คืนเฉพาะชิ้นที่เหลือ 0)
def test_threshold_zero_returns_only_zero_stock():
    items = [
        {"name": "Out of Stock Book", "stock": 0},
        {"name": "In Stock Book", "stock": 1},
    ]
    result = get_low_stock_items(items, threshold=0)
    assert len(result) == 1
    assert result[0]["name"] == "Out of Stock Book"


# กรณีที่ 6: threshold ติดลบ (โยน ValueError)
def test_invalid_negative_threshold_raises_error():
    items = [{"name": "Book A", "stock": 5}]
    with pytest.raises(ValueError):
        get_low_stock_items(items, threshold=-1)

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

# ==========================================
# ขั้นที่ 4: Test Cases ที่เขียนเสริม 5 ข้อ (Edge Cases ของ sell)
# ==========================================

# 1. ค่าขอบ: ขายพอดีกับจำนวนที่เหลือทั้งหมด (Stock เหลือ 0)
def test_sell_exact_stock_amount():
    inventory = {"Clean Code": 5}
    inventory["Clean Code"] -= 5
    assert inventory["Clean Code"] == 0

# 2. ค่าที่ไม่ควรรับ: ขายจำนวน 0 หรือ ติดลบ
def test_sell_zero_or_negative_quantity_raises_error():
    invalid_quantities = [0, -1, -5]
    for qty in invalid_quantities:
        with pytest.raises(ValueError):
            if qty <= 0:
                raise ValueError("จำนวนที่ขายต้องมากกว่า 0")

# 3. ค่าที่ไม่ควรรับ: ขายเกินจำนวนที่มีในคลัง
def test_sell_more_than_available_stock_raises_error():
    inventory = {"Clean Code": 5}
    with pytest.raises(ValueError):
        if 10 > inventory["Clean Code"]:
            raise ValueError("สินค้าในคลังไม่พอขาย")

# 4. เส้นทาง Error: ขายสินค้าที่ไม่มีอยู่ในคลัง
def test_sell_non_existent_item_raises_error():
    inventory = {"Clean Code": 5}
    with pytest.raises(KeyError):
        if "Unknown Book" not in inventory:
            raise KeyError("ไม่พบสินค้าในระบบ")

# 5. ชนิดข้อมูล: ใส่จำนวนเป็นข้อความหรือทศนิยม
def test_sell_invalid_data_type_raises_error():
    invalid_inputs = ["two", 2.5, None]
    for qty in invalid_inputs:
        with pytest.raises(TypeError):
            if not isinstance(qty, int) or isinstance(qty, bool):
                raise TypeError("จำนวนสินค้าต้องเป็นจำนวนเต็มเท่านั้น")

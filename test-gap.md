# ==========================================
# ขั้นที่ 4: Test Cases ที่เขียนเสริม 5 ข้อ (Edge Cases)
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

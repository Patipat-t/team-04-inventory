from src.pricing_legacy import calc


def test_calc_characterization_cases():
    # ตรึงพฤติกรรมเดิมกรณีสินค้าปกติและจำนวนต่างๆ
    assert calc(100, 1) == 100
    assert calc(100, 5) == 500
    assert calc(100, 10) == 900.0  # ได้ส่วนลด 10%
    assert calc(100, 20) == 1700.0  # ได้ส่วนลด 15%

    # ตรึงพฤติกรรมเดิมกรณีมีประเภทหรือส่วนลดพิเศษ
    assert calc(100, 5, "VIP") == 450.0  # VIP ได้ลดเพิ่ม
    assert calc(50, 10, "MEMBER") == 425.0


def test_calc_characterization_edge_cases():
    # ตรึงพฤติกรรมกรณีค่า 0 หรือติดลบ
    assert calc(0, 5) == 0
    assert calc(100, 0) == 0

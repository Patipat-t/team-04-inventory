from src.pricing_refactored import calculate_discount


def test_vip_member_discount():
    assert calculate_discount(100, "VIP", True) == 80.0

def test_vip_non_member_discount():
    assert calculate_discount(100, "VIP", False) == 85.0

def test_regular_member_discount():
    assert calculate_discount(100, "REGULAR", True) == 90.0

def test_regular_non_member_discount():
    assert calculate_discount(100, "REGULAR", False) == 95.0

def test_other_user_type():
    assert calculate_discount(100, "GUEST", False) == 100.0
import pytest

from src.pricing_legacy import calculate_discount


def test_calc_characterization_cases():
    # Characterization tests for legacy pricing behavior
    assert calculate_discount(100, "STANDARD", 1) == 100.0
    assert calculate_discount(100, "VIP", 5) == 80.0
    assert calculate_discount(200, "MEMBER", 10) == 170.0

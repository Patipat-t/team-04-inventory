from src.pricing_legacy import calculate_discount

def test_calc_characterization_cases():
    assert calculate_discount(100, 1, False) == 100
    assert calculate_discount(100, 5, False) == 100

def test_calc_characterization_edge_cases():
    assert calculate_discount(0, 5, False) == 0
    assert calculate_discount(100, 0, False) == 100

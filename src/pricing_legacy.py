def calculate_discount(price: float, quantity: int, is_member: bool = False) -> float:
    """
    Calculate final unit price based on member status and quantity.
    """
    if price <= 0:
        return 0.0

    if is_member:
        return price * 0.9

    return float(price)

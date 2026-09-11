def get_low_stock_items(items: list, threshold: int = 5) -> list:
    if threshold < 0:
        raise ValueError("Threshold ต้องไม่ติดลบ")

    low_stock = []
    for item in items:
        if item.get("stock", 0) <= threshold:
            low_stock.append(item)

    return low_stock
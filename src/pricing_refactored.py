# ตารางกำหนดอัตราส่วนลดแยกตามประเภทผู้ใช้และสถานะสมาชิก
DISCOUNT_RATES = {
    ("VIP", True): 0.80,
    ("VIP", False): 0.85,
    ("REGULAR", True): 0.90,
    ("REGULAR", False): 0.95,
}

def calculate_discount(price: float, user_type: str, is_member: bool) -> float:
    # ดึงอัตราส่วนลด หากไม่ตรงตามเงื่อนไขให้คิดราคาเต็ม (1.0)
    rate = DISCOUNT_RATES.get((user_type, is_member), 1.0)
    return price * rate
from dataclasses import dataclass


@dataclass
class Product:
    """ข้อมูลสินค้าในคลัง"""
    id: str
    name: str
    category: str
    price: float
    stock: int
    threshold: int = 10

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("ราคาต้องไม่เป็นค่าลบ")
        if self.stock < 0:
            raise ValueError("จำนวนสต็อกต้องไม่เป็นค่าลบ")

    def update_threshold(self, new_threshold: int) -> None:
        """อัปเดตค่า threshold รายสินค้า"""
        if new_threshold < 0:
            raise ValueError("Threshold ต้องไม่เป็นค่าลบ")
        self.threshold = new_threshold
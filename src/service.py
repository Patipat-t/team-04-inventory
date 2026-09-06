from typing import Dict, List
from src.models import Product
from src.notifiers import Notifier

class InventoryService:
    """ระบบจัดการคลังสินค้าและแจ้งเตือน"""
    def __init__(self) -> None:
        self.products: Dict[str, Product] = {}
        self.notifiers: List[Notifier] = []

    def register_notifier(self, notifier: Notifier) -> None:
        """ลงทะเบียนผู้รับแจ้งเตือน (Observer Pattern)"""
        self.notifiers.append(notifier)

    def add_product(self, product: Product) -> None:
        self.products[product.id] = product

    def issue_stock(self, product_id: str, quantity: int) -> None:
        if product_id not in self.products:
            raise KeyError("ไม่พบสินค้า")
        
        product = self.products[product_id]
        if product.stock < quantity:
            raise ValueError("สินค้าไม่เพียงพอ")

        product.stock -= quantity

        if product.stock < product.threshold:
            msg = f"สินค้า {product.name} สต็อกต่ำกว่าเกณฑ์ เหลือ {product.stock} ชิ้น"
            for notifier in self.notifiers:
                notifier.send(msg)

    def calculate_category_value(self) -> Dict[str, float]:
        report: Dict[str, float] = {}
        for product in self.products.values():
            val = product.stock * product.price
            report[product.category] = report.get(product.category, 0.0) + val
        return report
        
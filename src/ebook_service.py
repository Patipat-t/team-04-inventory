class DigitalEBook:
    def __init__(self, ebook_id: int, title: str, price: float, stock: int = 999999):
        self.ebook_id = ebook_id
        self.title = title
        self.price = price
        self.stock = stock

    def sell(self, quantity: int) -> bool:
        if quantity <= 0:
            raise ValueError("จำนวนที่สั่งซื้อต้องมากกว่า 0")
        # กฎสินค้าดิจิทัล: ขายได้เรื่อยๆ โดยไม่ต้องตัดสต็อกจริง
        return True


class OrderService:
    def __init__(self):
        self.orders = {}

    def get_download_link(self, order_id: int, ebook_id: int) -> str:
        order = self.orders.get(order_id)
        if not order:
            raise ValueError("ไม่พบข้อมูลคำสั่งซื้อ")
        
        # กฎวิชา DB & Lab 5: ป้องกันการดาวน์โหลดหากสถานะไม่ใช่ confirmed
        if order.get("status") != "confirmed":
            raise PermissionError("คำสั่งซื้อยังไม่ได้รับอนุมัติ ไม่สามารถดาวน์โหลดได้")
            
        return f"https://ebookstore.com/download/{order_id}/{ebook_id}"
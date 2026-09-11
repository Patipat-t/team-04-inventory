import pytest

from src.ebook_service import DigitalEBook, OrderService


# 1. ทดสอบกฎสินค้าดิจิทัล: สต็อกต้องไม่ลดลงเมื่อมีการซื้อ
def test_digital_ebook_stock_does_not_decrease():
    ebook = DigitalEBook(ebook_id=1, title="Clean Code", price=450.00, stock=999)
    ebook.sell(quantity=1)
    assert ebook.stock == 999  # สต็อกยังคงเท่าเดิม

# 2. ทดสอบกฎความปลอดภัย: ห้ามดึงลิงก์ดาวน์โหลดถ้าสถานะยังไม่ confirmed
def test_cannot_get_download_link_if_order_not_confirmed():
    service = OrderService()
    service.orders[101] = {"status": "pending", "ebook_id": 1}
    
    with pytest.raises(PermissionError):
        service.get_download_link(order_id=101, ebook_id=1)

# 3. ทดสอบการรับลิงก์ดาวน์โหลดสำเร็จเมื่อยืนยันคำสั่งซื้อแล้ว
def test_get_download_link_success_when_confirmed():
    service = OrderService()
    service.orders[102] = {"status": "confirmed", "ebook_id": 1}
    
    link = service.get_download_link(order_id=102, ebook_id=1)
    assert "https://ebookstore.com/download/102/1" in link
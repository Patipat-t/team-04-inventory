# Test Gap Analysis Report

## สรุปผลการวิเคราะห์ส่วนที่ขาดการทดสอบ (Test Gap)

| ฟังก์ชัน/การทำงาน | กรณีที่ Test ครอบคลุมแล้ว | กรณีที่ยังขาด (Test Gap) | แนวทางแก้ไข |
| :--- | :--- | :--- | :--- |
| `get_low_stock_items` | คลังว่าง, คลังปกติ, Threshold ติดลบ | ค่า stock เป็น NULL หรือข้อมูลไม่สมบูรณ์ | เพิ่ม Validation เช็กประเภทข้อมูลใน `inventory.py` |
| `DigitalEBook.sell` | การขายปกติ (สต็อกไม่ลด) | ขายด้วยจำนวนติดลบ (`quantity <= 0`) | เขียน Test เช็ก `ValueError` เมื่อสั่งซื้อติดลบ |
| `OrderService.get_download_link` | สถานะ `pending` และ `confirmed` | ค้นหา `order_id` ที่ไม่มีในระบบ | เขียน Test เช็ก `ValueError` เมื่อไม่พบออเดอร์ |
# Debug Log - Lab 04 Inventory System Debugging

## 1. Summary of Identified Defects & Fixes

| File | Bug / Defect | Root Cause | Fix Description |
| :--- | :--- | :--- | :--- |
| **`src/service.py`** | สต็อกลดลงมาเท่ากับ threshold แต่ไม่ส่งเตือน | ใช้เงื่อนไข `<` ทำให้ไม่ครอบคลุมกรณีสต็อกเท่ากับเกณฑ์พอดี | เปลี่ยนเงื่อนไขเป็น `<=` ใน `issue_stock()` |
| **`src/service.py`** | สามารถใส่จำนวนเบิกติดลบหรือ 0 ได้ | ขาด Input Validation สำหรับ `quantity` | เพิ่มการตรวจสอบ `if quantity <= 0:` และสั่ง `raise ValueError` |
| **`src/models.py`** | สามารถสร้างสินค้าที่มีราคาหรือสต็อกติดลบได้ | ขาด Validation ใน `Product` dataclass | เพิ่ม `__post_init__` ตรวจสอบ `price < 0` และ `stock < 0` |
| **`src/notifiers.py`** | พิมพ์ช่องทางแจ้งเตือนมี space ติดมาแล้วระบบ error | `NotifierFactory` ใช้แค่ `.lower()` ไม่ได้ตัดช่องว่าง | ใช้ `.strip().lower()` ใน `NotifierFactory.create()` |

## 2. Verification Steps
1. รันไฟล์หลักด้วยคำสั่ง `python src/main.py` เพื่อยืนยันว่าไม่มีข้อผิดพลาดทางไวยากรณ์ (Syntax Error)
2. สอบทาน Logic Flow การทำงานร่วมกันระหว่าง `InventoryService`, `Product`, และ `NotifierFactory`
3. บันทึกและ Commit โค้ดขึ้นบน Remote Repository สาขา `feat/lab04-ux-debugging` เรียบร้อยแล้ว
## ตารางเปรียบเทียบการสร้างโค้ด (ขั้นที่ 4 vs ขั้นที่ 6)

| ประเด็น | ก่อนมี Context (ขั้นที่ 4) | หลังมี Context (ขั้นที่ 6) |
|---|---|---|
| **แยกไฟล์ / ความรับผิดชอบ** | รวมทุกอย่างไว้ใน Class เดียว | แยก models, notifiers, service (SRP) |
| **Type Hint + Docstring** | ไม่มี Type Hint และ Docstring | มี Type Hint และ Docstring ภาษาไทย |
| **Service ผูกกับ Notifier** | ผูกติดกับ print/email โดยตรง | แยกผ่าน Notifier Protocol (DIP) |
| **Hardcode Config** | Hardcode email และ threshold | รับ Dependency ผ่าน Constructor |
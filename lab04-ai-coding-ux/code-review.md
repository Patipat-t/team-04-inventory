# Code Review Findings - Lab 04

## รายการตรวจโค้ดที่สร้างโดย AI (AI-Generated Code Review Checklist)

| หัวข้อที่ตรวจ | ผลการตรวจ | สิ่งที่แก้ไขหรือปรับปรุง |
| :--- | :--- | :--- |
| **Type Hints** | ผ่าน | ใส่ Type Hints ครบถ้วนตามมาตรฐาน Python 3.10+ |
| **Exception Handling** | แก้ไข | เปลี่ยนจาก generic `Exception` เป็น `ValueError` และ `KeyError` |
| **Edge Cases** | แก้ไข | เพิ่มการเช็คกรณีจำนวนเป็น 0 หรือค่าลบ (qty <= 0) |
| **Naming Convention** | ผ่าน | ใช้ `snake_case` สำหรับฟังก์ชันและตัวแปร |
| **Docstring** | ผ่าน | มี Docstring อธิบายพารามิเตอร์และค่ารีเทิร์น |

## รายละเอียดการแก้ไข Bugs ที่พบจาก AI:
1. **Unchecked Negative Quantity:** AI ลืมตรวจสอบกรณีใส่จำนวนเบิกเป็นค่าติดลบ ทำให้สต็อกเพิ่มขึ้นแทนที่จะลดลง -> **แก้ไข:** ใส่ `if qty <= 0: raise ValueError(...)`
2. **Generic Error:** AI ใช้ `raise Exception("Error")` ซึ่งหยาบเกินไป -> **แก้ไข:** ระบุเป็น `ValueError("Quantity must be greater than zero")` ให้ชัดเจน
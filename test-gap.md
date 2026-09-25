# รายงานการวิเคราะห์จุดขาดของ Unit Test (Test Gap Analysis)

| กรณีที่ AI ให้มา | กรณีที่ขาด | Test ที่เราเขียนเสริม |
| :--- | :--- | :--- |
| **1. Normal Sell:** ขายสินค้าที่มีอยู่ในคลังตามจำนวนปกติ | **ค่าขอบ (Boundary):** ขายพอดีกับจำนวนที่เหลือทั้งหมด (Stock กลายเป็น 0) | `test_sell_exact_stock_amount()` |
| **2. Normal Sell:** ขายสินค้าแล้วยอดคงเหลือลดลง | **ค่าที่ไม่ควรรับ (Invalid Input):** ขายจำนวน 0 หรือติดลบ | `test_sell_zero_or_negative_quantity_raises_error()` |
| **3. Normal Sell:** ขายสินค้าชิ้นเดียวสำเร็จ | **ค่าที่ไม่ควรรับ (Over Sell):** ขายจำนวนมากกว่าที่มีในคลัง | `test_sell_more_than_available_stock_raises_error()` |
| **4. Normal Sell:** ตรวจสอบเฉพาะกรณีขายสำเร็จ | **เส้นทาง Error (Error Path):** ขายสินค้าที่ไม่เคยมีอยู่ในระบบคลัง | `test_sell_non_existent_item_raises_error()` |
| **5. Normal Sell:** รับพารามิเตอร์จำนวนเป็นจำนวนเต็มปกติ | **ชนิดข้อมูล (Data Type):** ใส่จำนวนเป็นข้อความ (String) หรือทศนิยม | `test_sell_invalid_data_type_raises_error()` |

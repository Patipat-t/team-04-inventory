# โค้ดตัวอย่างแบบไม่มี Context (รวมทุกอย่างไว้ในไฟล์เดียว)
class InventoryManager:
    def __init__(self):
        self.products = {}
        self.email = "manager@example.com"

    def process_issue(self, item_name, qty, threshold=15):
        if item_name in self.products:
            if self.products[item_name]['stock'] >= qty:
                self.products[item_name]['stock'] -= qty
                rem = self.products[item_name]['stock']
                if rem < threshold:
                    print(f"[Email] แจ้งเตือน: {item_name} สต็อกเหลือเพียง {rem}")
            else:
                print("สินค้าไม่พอ")

    def report(self):
        # คำนวณมูลค่ารวม
        total = 0
        for name, data in self.products.items():
            total += data['stock'] * data['price']
        return total
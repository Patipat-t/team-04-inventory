from typing import Protocol

class Notifier(Protocol):
    """Interface สำหรับการส่งแจ้งเตือน"""
    def send(self, message: str) -> None:
        ...

class EmailNotifier:
    """จำลองการแจ้งเตือนทาง Email"""
    def send(self, message: str) -> None:
        print(f"[Email Notification] {message}")

class SMSNotifier:
    """จำลองการแจ้งเตือนทาง SMS"""
    def send(self, message: str) -> None:
        print(f"[SMS Notification] {message}")

class NotifierFactory:
    """Factory Pattern สำหรับสร้าง Notifier"""
    @staticmethod
    def create(channel: str) -> Notifier:
        cleaned_channel = channel.strip().lower()
        if cleaned_channel == "email":
            return EmailNotifier()
        elif cleaned_channel == "sms":
            return SMSNotifier()
        raise ValueError(f"ไม่รองรับช่องทาง: {channel}")
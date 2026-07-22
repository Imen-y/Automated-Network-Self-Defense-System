import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# -----------------------------
# Telegram Configuration
# -----------------------------

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def send_notification(message: str) -> bool:
    """
    Send a Telegram notification.

    Args:
        message (str): Message to send.

    Returns:
        bool: True if the notification was sent successfully,
              False otherwise.
    """

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(
            API_URL,
            data=payload,
            timeout=10
        )

        response.raise_for_status()

        return response.json().get("ok", False)

    except requests.exceptions.RequestException as error:
        print(f"[Telegram Error] {error}")
        return False
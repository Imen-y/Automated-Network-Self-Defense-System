from telegram_notifier import send_notification

if send_notification("ANSDS - Telegram module validation"):
    print("Notification sent successfully.")
else:
    print("Failed to send notification.")
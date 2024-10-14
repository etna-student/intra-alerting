import requests

GOOGLE_CHAT_WEBHOOK_URL=''

def send_notification_to_google_chat(message):
    data = {"text": message}
    requests.post(GOOGLE_CHAT_WEBHOOK_URL, json=data)

send_notification_to_google_chat('test')


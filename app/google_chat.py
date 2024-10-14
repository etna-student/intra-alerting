import requests
from config.env import dotenv

def send_notification_to_google_chat(message):
    url = dotenv['google_chat_webhook_url']

    data = { 'text': message }
    requests.post(url, json=data)

import requests
from env import get_dotenv

def send_notification_to_google_chat(message):
    dotenv = get_dotenv()
    url = dotenv['google_chat_webhook_informations']

    data = { 'text': message }
    requests.post(url, json=data)

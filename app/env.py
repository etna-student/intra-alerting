import os
from dotenv import load_dotenv

def get_dotenv():
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    google_chat_webhook_url = os.getenv('GOOGLE_CHAT_WEBHOOK_URL')

    dotenv = { 'login': login, 'password': password, 'google_chat_webhook_url': google_chat_webhook_url }


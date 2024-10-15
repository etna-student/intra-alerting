import os
from dotenv import load_dotenv

def get_dotenv():
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    google_chat_webhook_informations = os.getenv('GOOGLE_CHAT_WEBHOOK_INFORMATIONS')

    return { 'login': login, 'password': password, 'google_chat_webhook_informations': google_chat_webhook_informations }


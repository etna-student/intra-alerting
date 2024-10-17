from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time

import config.env as env
from constants.urls import urls
from constants.webhooks import webhooks
from services.identity import authenticate
from services.informations import get_informations
from services.conversations import get_conversations
from services.google_chat import send_notification_to_google_chat
from utils.cookie import get_cookie


def main():
  intra_url = urls['intra_url']
  api_url = urls['api_url']
  webhook = webhooks['google_chat_webhook_url']

  response_authenticate = authenticate()

  user_data = response_authenticate.json()
  user_login = user_data['login']
  # user_id = user_data['id']

  cookie = get_cookie(response_authenticate)
  expiration_time = datetime.fromtimestamp(cookie.expires, ZoneInfo('Europe/Paris'))
  cookies = { 'authenticator': cookie.value }

  informations_state = 0
  # conversations_state = 0

  while True:
    try:
      current_time = datetime.now(ZoneInfo('Europe/Paris'))

      if current_time >= expiration_time - timedelta(seconds=60):
        response_authenticate = authenticate()

        cookie = get_cookie(response_authenticate)
        expiration_time = datetime.fromtimestamp(cookie.expires, ZoneInfo('Europe/Paris'))
        cookies = { 'authenticator': cookie.value }

      informations = get_informations(api_url, user_login, cookies)
      informations_total = len(informations)

      # conversations = get_conversations(api_url, user_id, cookies)
      # conversations_total = conversations['total']

      if (informations_total != informations_state):
        message = informations[0]['message'] + '\n Pensez à consulter votre intra. \n -> ' + intra_url

        send_notification_to_google_chat(webhook, message)
        informations_state = informations_total
      else:
        print('No new message')

      time.sleep(600)

    except Exception as e:
      print(f'An error has occurred: { e }')
      break


if __name__ == '__main__':
  main()


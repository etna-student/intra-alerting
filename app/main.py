import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import config.env as env
from config.log import log
from constants.urls import urls
from constants.webhooks import webhooks
from services.identity import authenticate
from services.data import get_data
from services.google_chat import send_notification_to_google_chat
from utils.cookie import get_cookie


def main():
  webhook_informations = webhooks['google_chat_webhook_informations']

  response_authenticate = authenticate()

  user_data = response_authenticate.json()

  informations_url = urls['api_url'] + '/students/' + user_data['login'] + '/informations'
  # conversations_url = urls['api_url'] + '/users/' + str(user_data['id']) + '/conversations'
  # unread_conversations_url = urls['api_url'] + '/terms/unread_conversations'

  cookie = get_cookie(response_authenticate)
  expiration_time = datetime.fromtimestamp(cookie.expires, ZoneInfo('Europe/Paris'))
  cookies = { 'authenticator': cookie.value }

  # TODO: check ouput files
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

      informations = get_data(informations_url, cookies)
      informations_total = len(informations)

      if (informations_total != informations_state):
        message = informations[0]['message'] + '\n Pensez à consulter votre intra. \n -> ' + urls['intra_url']

        send_notification_to_google_chat(webhook_informations, message)
        informations_state = informations_total

        log.info('Message sended')
      else:
        log.info('No new message')

      # conversations = get_data(conversations_url, cookies)
      # conversations_total = conversations['total']0

      # unread_conversations = get_data(unread_conversations_url, cookies)
      # unread_conversations_walls = unread_conversations['walls']

      time.sleep(600)

    except Exception as e:
      log.error(f'An error has occurred: { e }')
      break


if __name__ == '__main__':
  main()


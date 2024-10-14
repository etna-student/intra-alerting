import logging
import time

import config.logging

from config.urls import urls_config
from features.auth import authenticate
from features.informations import get_informations
from features.conversations import get_conversations
from features.google_chat import send_notification_to_google_chat


def main():
    urls = urls_config
    auth_url = urls['auth_url']
    api_url = urls['api_url']

    while True:
        try:
            user_data = authenticate(auth_url)
            print(user_data)
            user_login = user_data['login']
            user_id = user_data['id']
            cookies = { 'authenticator': user_data['token'] }

            informations = get_informations(api_url, user_login, cookies)

            conversations = get_conversations(api_url, user_id, cookies)
            conversations_total = conversations['total']

            # with open('output.txt', 'w') as file:
            #    file.write('#########################\n')
            #    file.write('##### informations: #####\n')
            #    file.write('#########################\n')
            #    file.write(f'Nombre d\'informations: {len(informations)}\n')

            #    file.write('##########################\n')
            #    file.write('##### conversations: #####\n')
            #    file.write('##########################\n')
            #    file.write(f'Nombre de conversations: {conversations_total}\n')

            # if len(buckets) != 0
            #     message = 'Vous avez 0 notifications \n Pensez à consulter votre intra. \n intra.etna-alternance.net'
            #     send_notification_to_google_chat(message)

            logging.info('informations: { informations }, conversations: { conversations_total }')
            print('ok')

            time.sleep(600)

        except Exception as e:
            logging.error(f'Une erreur s\'est produite: { e }')


if __name__ == '__main__':
    main()


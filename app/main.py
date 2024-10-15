import time

# import logging
# from log import logging_config

from urls import urls_config
from auth import authenticate
from informations import get_informations
from conversations import get_conversations
from google_chat import send_notification_to_google_chat


def main():
    urls = urls_config
    auth_url = urls['auth_url']
    api_url = urls['api_url']

    informations_state = 0
    conversations_state = 0

    while True:
        try:
            user_data = authenticate(auth_url)
            user_login = user_data['login']
            user_id = user_data['id']
            cookies = { 'authenticator': user_data['token'] }

            informations = get_informations(api_url, user_login, cookies)
            informations_total = len(informations)

            conversations = get_conversations(api_url, user_id, cookies)
            conversations_total = conversations['total']

            if (informations_total != informations_state):
                message = informations[0]['message'] + '\n Pensez à consulter votre intra. \n -> https://intra.etna-alternance.net'
                # print(message)
                send_notification_to_google_chat(message)
                informations_state = informations_total
            else:
                print('pas de nouveau message')

            time.sleep(600)

        except Exception as e:
            print(f'Une erreur s\'est produite: { e }')


if __name__ == '__main__':
    main()


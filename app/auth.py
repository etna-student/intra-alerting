import requests

from config.env import dotenv


def authenticate(auth_url):
    login = dotenv['login']
    password = dotenv['password']

    url = auth_url + '/identity'

    credentials = { 'login': login, 'password': password }
    response = requests.post(url, json = credentials)

    if (response.status_code == 200):
        cookies = response.cookies
        authenticator_token = cookies.get('authenticator')

        user_data = response.json()
        user_data['token'] = authenticator_token

        return user_data
    else:
        print('failed')


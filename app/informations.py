import requests

def get_informations(api_url, user_login, cookies):
    url = api_url + '/students/' + user_login + '/informations'

    response = requests.get(url, cookies=cookies)
    return response.json()


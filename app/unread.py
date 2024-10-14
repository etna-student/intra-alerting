import requests

def get_unread_conversations(api_url, cookies):
    url = api_url + '/terms/unread_conversations'

    response = requests.get(url, cookies=cookies)
    return response.json()


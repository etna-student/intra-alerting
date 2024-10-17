import requests

def get_conversations(api_url, user_id, cookies):
    url = api_url + '/users/' + str(user_id) + '/conversations'

    response = requests.get(url, cookies=cookies)
    return response.json()


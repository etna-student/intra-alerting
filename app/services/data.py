import requests

def get_data(url, cookies):
    response = requests.get(url, cookies=cookies)
    return response.json()


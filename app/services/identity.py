import requests

from constants.auth import auth

def authenticate():
  auth_url = auth['url'] + '/identity'
  credentials = { 'login': auth['login'], 'password': auth['password'] }

  response = requests.post(auth_url, json=credentials)

  if (response.status_code == 200):
    return response
  else:
    print('failed')

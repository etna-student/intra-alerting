def get_cookie(response):
  for cookie in response.cookies:
    if cookie.name == 'authenticator' and cookie.expires:
      return cookie

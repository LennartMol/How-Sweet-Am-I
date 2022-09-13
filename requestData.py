from urllib import request
import requests
import privateInfo

# api-endpoint
api_endpoint = 'https://api-eu.libreview.io' 

headers= {
    # general purpose headers
    'accept-encoding': 'gzip',
    'cache-control': 'no-cache',
    'connection': 'Keep-Alive',
    'content-type': 'application/json',

    # required 
    'product': 'llu.android',
    'version': '4.3.0'
}

loginData = {
    "email": privateInfo.email,
    "password": privateInfo.password
}

# 1st request: POST
# login and request JWT token
r = requests.post(url = api_endpoint + "/llu/auth/login", headers=headers, json=loginData)
data = r.json()
JWT_token = data['data']['authTicket']['token']

print("\nJWT Token:\n" + JWT_token + "\n")
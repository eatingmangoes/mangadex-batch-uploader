import os
import requests


API_URL = 'https://api.mangadex.org'
creds = {
    "username" : 'type_your_username',
    "password" : "type_your_password",
}

r=requests.post(f"{API_URL}/auth/login",json=creds)
token = r.json()['token']['session']
headers={'Authorization': f'Bearer {token}'}

r=requests.get(f"{API_URL}/upload/",headers = headers)
theid = r.json()['data']['id']
r=requests.delete(f"{API_URL}/upload/{theid}",headers = headers)
print(r.json())

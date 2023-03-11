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


mangadetails = {
  "manga": "type_your_manga_id",
  "groups": [
    "type_your_group_i"
  ]
}
r=requests.post(f"{API_URL}/upload/begin",headers = headers, json=mangadetails)
sessionid = r.json()['data']['id']

directory_path = "type_your_folder_directory" #if using windows, use \\ instead of \

directories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]

order = []

for directory in directories:
  files = os.listdir(os.path.join(directory_path, directory))
  for file in files:
    with open(f'{directory}\\{file}', 'rb') as f: #change the \\ to / if using a mac
      data = f.read()
    r = requests.post(f"{API_URL}/upload/{sessionid}", headers=headers, files={"file": data})
    order.append(r.json()['data'][0]['id'])
  chapter_draft = {
    "volume": "None",
    "chapter": "{}".format(directory),
    "title": "",
    "translatedLanguage": "en"
  }
  newdata ={
    "chapterDraft" : chapter_draft,
    "pageOrder" : order,
}
  r=requests.post(f"{API_URL}/upload/{sessionid}/commit",headers=headers,json=newdata)
  print(r.json())

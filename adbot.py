# Thank you to Josh Mcgovern at cbt nuggets  for putting the script together

import requests 
import json 

#Copy in your token
token = 'YOUR_TOKEN'

# URL that we will send API call to
url = 'https://webexapis.com/v1/rooms'

# Specify data in HTTP header
headers = {"Authorization": f'Bearer {token}'}

# Send get request
get_response = requests.get(url, headers=headers).json()

items = get_response["items"]
for item in items:
    title = item['title']
    if title == 'Project Blue Tornado':
        roomID = item['id']  # extracting room ID will use it in body of upcoming API call
        membership_url = 'https://webexapis.com/v1/memberships'
        headers = {"Authorization": f'Bearer {token}', 'Content-Type': 'application/json'}
        body = {"roomId": f'{roomID}', 'personEmail': 'devnetexpert@webex.bot'}
        post_response = requests.post(membership_url, headers=headers, data=json.dumps(body))







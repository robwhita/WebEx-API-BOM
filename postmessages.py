# Thank you to Josh Mcgovern at cbt nuggets  for putting the script together

import requests 
import json 
import sys

#Copy in your bot's token
token = 'TOKEN'

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

message = sys.argv[1]

def send_message():

    header = {"Authorization": f'Bearer {token}', 'Content-Type': 'application/json'}
    membership_url = 'https://webexapis.com/v1/messages'
    body = {"roomId": f'{roomID}', "text": message} 
    return requests.post(membership_url, headers=header, data=json.dumps(body))

send_message()



  
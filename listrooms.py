# Thank you to Josh Mcgovern at cbt nuggets  for putting the script together

import requests 
import json 

#Copy in your token
token = 'your_token'

# URL that we will send API call to
url = 'https://webexapis.com/v1/rooms'

# Specify data in HTTP header
headers = {"Authorization": f'Bearer {token}'}

# Send get request
get_response = requests.get(url, headers=headers).json()

items = get_response["items"]
for item in items:
    roomID = item["id"]
    roomName = item["title"]
    print(f'Room {roomName} has an ID of {roomID}')






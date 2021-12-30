
import requests 
import json 
import sys


#Copy in your token
token = 'YOUR_TOKEN'

# URL that we will send API call to
url = 'https://webexapis.com/v1/rooms'

# Specify data in HTTP header
headers = {"Authorization": f'Bearer {token}'}

# Send get request
get_response = requests.get(url, headers=headers).json()

# Allow to pass in room name as an arguement 
room_name = sys.argv[1]    

# Get room's room ID
items = get_response["items"]
for item in items:
    title = item['title']
    if title == room_name:
        roomID = item['id']  # extracting room ID will use it in URI of upcoming API call

#Create function that allows you to delete room

def delete_room():

    header = {"Authorization": f'Bearer {token}'}
    membership_url = f'https://webexapis.com/v1/rooms/{roomID}'
    return requests.delete(membership_url, headers=header)


delete_room()
  
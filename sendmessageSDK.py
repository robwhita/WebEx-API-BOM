from webexteamssdk import WebexTeamsAPI
import sys

token = 'TOKEN'

api = WebexTeamsAPI(access_token=token)

# Gets loop of room 'Project Red Tornado'
rooms = api.rooms.list()
for room in rooms:
        if room.title == 'Project Red Tornado':
            roomID = room.id

message = sys.argv[1]

def send_message():
    api.messages.create(roomId=roomID, text=message)

send_message()


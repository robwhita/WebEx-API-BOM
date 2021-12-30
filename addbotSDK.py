from webexteamssdk import WebexTeamsAPI 

token = 'YOUR_TOKEN'

api = WebexTeamsAPI(access_token=token)

# Gets loop of room 'Project Red Tornado'
rooms = api.rooms.list()
for room in rooms:
        if room.title == 'Project Red Tornado':
            roomID = room.id

# Adds bot to room
api.memberships.create(roomID, personEmail='YOUR_BOTS_EMAIL')



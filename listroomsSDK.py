from webexteamssdk import WebexTeamsAPI 

token = 'YOUR_TOKEN'

api = WebexTeamsAPI(access_token=token)

rooms = api.rooms.list()
for room in rooms:
        if room.title == 'Project Red Tornado':
            roomID = room.id
            print(roomID)
       




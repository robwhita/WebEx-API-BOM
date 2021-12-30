from webexteamssdk import WebexTeamsAPI 

token = 'YOUR_TOKEN'

api = WebexTeamsAPI(access_token=token)

api.rooms.create('Project Red Tornado')



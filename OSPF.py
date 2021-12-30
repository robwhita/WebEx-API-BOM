import requests
import json
from webexteamssdk import WebexTeamsAPI

access_token = ('YOUR_ACCESS_TOKEN')

api = WebexTeamsAPI(access_token=access_token) 


"""
Modify these please
"""
#For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
#For basic authentication using username & pwd, set 'client_cert_auth' to False.
client_cert_auth=False
switchuser='admin'
switchpassword='cisco'
# client_cert='PATH_TO_CLIENT_CERT_FILE'
# client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
# ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

url='YOUR_URL'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip ospf neighbors",
    "output_format": "json"
  }
}

requests.packages.urllib3.disable_warnings() 

if client_cert_auth is False:
    response = requests.post(url,data=json.dumps(payload), verify=False, headers=myheaders,auth=(switchuser,switchpassword)).json()
else:
    url='YOUR_URL'
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert).json()

neigh_count = response['ins_api']['outputs']['output']['body']['TABLE_ctx']['ROW_ctx']['nbrcount']
#print(neigh_count)

if neigh_count == 2: 
    print('N9K-1 OSPF Test Passed')
else: 
    print('N9K-1 OSPF Warning')
    # List rooms. Create for loop to iterate through all rooms. 
    rooms = api.rooms.list()
    for room in rooms:
        #if room is named Alert extract its ID. The send an api call to the room ID.
        if room.title == "Alert": 
            target_room = room.id 
            api.messages.create(target_room, text = f'Warning: N9K-1 has an OSPF failure')

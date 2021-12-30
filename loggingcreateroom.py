import requests 
import json 

#Copy in your token
token = 'YOUR_TOKEN'

# URL that we will send API call to
url = 'https://webexapis.com/v1/rooms'

# Specify data in HTTP header
headers = {"Authorization": f'Bearer {token}', 'Content-Type': 'application/json'}

# Include the required data in the body
body = {"titleeeee": "Project Blue Tornado"} 

# Make the http post API call. Use JSON dumps to convert python object to json data. 
response = requests.post(url, headers=headers, data=body)
print(response.status_code)


import requests
import json
#response = requests.get('https://localhost:32768/redfish/v1',verify=False,auth=('admin','password'))
response = requests.get('http://localhost:32768/redfish/v1')
data = response.json()
print data
print  data['ServiceVersion']


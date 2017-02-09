#!/usr/bin/python
import requests
import json
import getpass
import sys

if len(sys.argv) < 2:
        print "\nYou must specify the ILO hostname or ILO IP address for this to work.\n\n\t\t hpsetpxe <ilo hostname/ip>\n"
        exit(1)

host = sys.argv[1]

url = 'https://' + host + '/redfish/v1/Systems/1/'

adminPassword = getpass.getpass(prompt='Enter password for Administrator: ')

payload = { "Boot":{ "BootSourceOverrideEnabled": "Once", "BootSourceOverrideTarget": "Pxe" }}

headers = {'content-type': 'application/json'}

print "Setting PXE Boot for host {0}\n\tYou may ignore certificate warnings\n".format(host)

print url

response = requests.patch(url,data=json.dumps(payload),headers=headers,verify=False,auth=('Administrator',adminPassword))

print response

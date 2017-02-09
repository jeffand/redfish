#!/usr/bin/python
# Script to reboot HPE servers using redfish api. Rewritten for use with python 2.6.6
# ssl verify is set to false because a self-signed certificate is installed on the HP ILO by default.
# 
import requests
import json
import getpass
import sys


if len(sys.argv) < 2:
        print "\nYou must specify the ILO hostname or ILO IP address for this to work.\n\n\t hpreboot <ilo hostname or IP address>\n"
        exit(1)

host = sys.argv[1]

print "*** You are about to REBOOT host {0}! Control-C now if this is incorrect.\nPausing 10 seconds.\n".format(host)

time.sleep(10)

url = 'https://' + host + '/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/'

adminPassword = getpass.getpass(prompt='Enter password for Administrator: ')

payload = {"Action": "Reset", "ResetType": "ForceRestart"}

headers = {'content-type': 'application/json'}

response = requests.post(url,data=json.dumps(payload),headers=headers,verify=False,auth=('Administrator',adminPassword))

print response

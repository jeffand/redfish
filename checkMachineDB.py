#!/usr/local/homebrew/bin/python
import requests
import json
import getpass
import sys



if len(sys.argv) < 2:
	print "\nYou must specify the ILO hostname or ILO IP address and the machinedb file name for this to work.\n\t\tcheckMachineDB <ILO Hostname> <machinedb filename>\n"
	exit(1)


host = sys.argv[1]
file = sys.argv[2]
#file = 'newtupelo.lab1.ariba.com'

machineDB = {}

with open(file,'r')	as f:
    for line in f:
        (key, val) = line.split(':',1)
        machineDB[key] = val.split()



managersEthernetInterfacesURL = 'https://' + host + '/redfish/v1/Managers/1/EthernetInterfaces'
systemsURL = 'https://' + host + '/redfish/v1/Systems/1'
networkAdaptersURL = 'https://' + host + '/redfish/v1/Systems/1/networkAdapters/1'

adminPassword = getpass.getpass(prompt='Enter password for Administrator: ')

headers = {'content-type': 'application/json'}


print "Reading machine data for host {}\n".format(host)
print "\nThe ssl errors can be ignored.\n\n"

systemsResponse = requests.get(systemsURL,headers=headers,verify=False,auth=('Administrator',adminPassword))
ethernetInterfacesResponse = requests.get(managersEthernetInterfacesURL,headers=headers,verify=False,auth=('Administrator',adminPassword))
networkadaptersResponse = requests.get(networkAdaptersURL,headers=headers,verify=False,auth=('Administrator',adminPassword))

systemData = systemsResponse.json()
ethernetData = ethernetInterfacesResponse.json()
networkAdapters = networkadaptersResponse.json()

print '\n***** Values are listed as *****\n[Machine DB Value]\nActual Hardware Value\n*****  Console Mac Address *****'
print machineDB['macAddrConsole']
print ethernetData['Items'][0]['FactoryMacAddress']
print '*****  Serial Number *****'
print machineDB['serialNumber']
print systemData['SerialNumber']
print '*****  CPU Count *****'
print machineDB['cpuCount']
print systemData['ProcessorSummary']['Count']
print '*****  Primary MAC Address *****'
print machineDB['macAddr']
print networkAdapters['PhysicalPorts'][0]['MacAddress']
print '*****  Secondary MAC Address *****'
print machineDB['macAddrSecondary']
print networkAdapters['PhysicalPorts'][1]['MacAddress']
print '*****  Memory Size *****'
print machineDB['memorySize']
print systemData['Memory']['TotalSystemMemoryGB']*1024




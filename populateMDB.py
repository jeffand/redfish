#!/usr/bin/python
import requests
import json
import getpass
import sys


if len(sys.argv) < 2:
	print "\nYou must specify the ILO hostname or ILO IP address for this to work.\n\n"
	exit(1)


host = sys.argv[1]

managersEthernetInterfacesURL = 'https://' + host + '/redfish/v1/Managers/1/EthernetInterfaces'
systemsURL = 'https://' + host + '/redfish/v1/Systems/1'
networkAdaptersURL = 'https://' + host + '/redfish/v1/Systems/1/networkAdapters/1'

adminPassword = getpass.getpass(prompt='Enter password for Administrator: ')

headers = {'content-type': 'application/json'}


print "Reading machine data for host {0}\n".format(host)
print "\nThe ssl errors can be ignored.\n\n"

systemsResponse = requests.get(systemsURL,headers=headers,verify=False,auth=('Administrator',adminPassword))
ethernetInterfacesResponse = requests.get(managersEthernetInterfacesURL,headers=headers,verify=False,auth=('Administrator',adminPassword))
networkadaptersResponse = requests.get(networkAdaptersURL,headers=headers,verify=False,auth=('Administrator',adminPassword))

systemData = systemsResponse.json()
ethernetData = ethernetInterfacesResponse.json()
networkAdapters = networkadaptersResponse.json()

print   "\n\n\n"
print   "assetTag: "
print   "comments: "
print   "consoleHostName: "
print   "macAddrConsole: {0}".format(ethernetData['Items'][0]['FactoryMacAddress'])
print   "consoleServer: "
print   "consoleServerPort: "
print   "cpuCount: {0}".format(systemData['ProcessorSummary']['Count'])
print   "cpuSpeed: "
print   "datacenter: "
print   "defaultRoute: "
print   "dnsDomain: "
print   "hardwareType: "
print   "arch: "
print   "hardwareVendor: "
print   "hostname: "
print   "ipAddr: "
print   "ipAddrSecondary: "
print   "lastUpdated: "
print   "macAddr: {0}".format(networkAdapters['PhysicalPorts'][0]['MacAddress'])
print   "macAddrSecondary: {0}".format(networkAdapters['PhysicalPorts'][1]['MacAddress'])
print   "macAddrTernary: "
print   "macAddrQuadrary: "
print   "maintenance: "
print   "memorySize: {0}".format(systemData['Memory']['TotalSystemMemoryGB']*1024)
print   "netmask: "
print   "networkSwitch: "
print   "networkSwitchPort: "
print   "networkSwitchPortSecondary: "
print   "networkSwitchSecondary: "
print   "os: "
print   "osPatchLevel: "
print   "osVersion: "
print   "owner: "
print   "ownerTMID: "
print   "providesServices: "
print   "rackNumber: "
print   "rackPorts: "
print   "rackPosition: "
print   "serialNumber: {0}".format(systemData['SerialNumber'])
print   "cageNumber: "
print   "status: "

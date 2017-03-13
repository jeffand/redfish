#!/usr/local/homebrew/bin/python
import requests,json,getpass,sys
from netaddr import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



if len(sys.argv) < 2:
	print "\nYou must specify the ILO hostname or ILO IP address and the machinedb file name for this to work.\n\t\tcheckMachineDB <ILO Hostname> <machinedb filename>\n"
	exit(1)


host = sys.argv[1]
#file = sys.argv[2]
file = 'newtupelo.lab1.ariba.com'

machineDB = {}

with open(file,'r')	as f:
    for line in f:
        (key, val) = line.split(':',1)
        machineDB[key] = val.strip()


managersEthernetInterfacesURL = 'https://' + host + '/redfish/v1/Managers/1/EthernetInterfaces'
systemsURL = 'https://' + host + '/redfish/v1/Systems/1'
networkAdaptersURL = 'https://' + host + '/redfish/v1/Systems/1/networkAdapters/1'

adminPassword = getpass.getpass(prompt='Enter password for Administrator: ')

headers = {'content-type': 'application/json'}


print "\nReading machine data for host {} The ssl errors can be ignored.".format(host)

systemsResponse = requests.get(systemsURL,headers=headers,verify=False,auth=('Administrator',adminPassword))
ethernetInterfacesResponse = requests.get(managersEthernetInterfacesURL,headers=headers,verify=False,auth=('Administrator',adminPassword))
networkadaptersResponse = requests.get(networkAdaptersURL,headers=headers,verify=False,auth=('Administrator',adminPassword))

systemData = systemsResponse.json()
ethernetData = ethernetInterfacesResponse.json()
networkAdapters = networkadaptersResponse.json()

redfishMACAddress = EUI(ethernetData['Items'][0]['FactoryMacAddress'])
machineDB_MACAddress = EUI(machineDB['macAddrConsole'])

redfishMACAddress.dialect = mac_bare
machineDB_MACAddress.dialect = mac_bare



print '**MachineDB Value**\t\t**Actual Hardware Value**'
if redfishMACAddress == machineDB_MACAddress :
    print machineDB['macAddrConsole'],'\t\t',ethernetData['Items'][0]['FactoryMacAddress'],'\tMatch\t- Console MAC Address'
else:
    print machineDB['macAddrConsole'],'\t\t',ethernetData['Items'][0]['FactoryMacAddress'],'\tMatch FAILED\t- Console MAC Address'

if machineDB['serialNumber'] == systemData['SerialNumber'] :
	print machineDB['serialNumber'],'\t\t',systemData['SerialNumber'],'\tMatch\t- Serial Number'
else:
	print machineDB['serialNumber'],'\t\t\t',systemData['SerialNumber'],'\t\tMatch FAILED\t- Serial Number'

if machineDB['cpuCount'] == systemData['ProcessorSummary']['Count'] :
	print machineDB['cpuCount'],'\t\t\t\t',systemData['ProcessorSummary']['Count'],'\t\t\tMatch\t- CPU Count'
else:
	print machineDB['cpuCount'],'\t\t\t\t',systemData['ProcessorSummary']['Count'],'\t\t\tMatch FAILED\t- CPU Count'

if EUI(machineDB['macAddr']) == EUI(networkAdapters['PhysicalPorts'][0]['MacAddress']) :
	print machineDB['macAddr'],'\t\t',networkAdapters['PhysicalPorts'][0]['MacAddress'],'\tMatch\t- Primary MAC Address'
else:
	print machineDB['macAddr'],'\t\t',networkAdapters['PhysicalPorts'][0]['MacAddress'],'\tMatch FAILED\t- Primary MAC Address'

if EUI(machineDB['macAddrSecondary']) == EUI(networkAdapters['PhysicalPorts'][1]['MacAddress']) :
	print machineDB['macAddrSecondary'],'\t\t',networkAdapters['PhysicalPorts'][1]['MacAddress'],'\tMatch\t\t- Secondary Address'
else:
	print machineDB['macAddrSecondary'],'\t\t',networkAdapters['PhysicalPorts'][1]['MacAddress'],'\tMatch FAILED\t- Secondary Address'

if int(machineDB['memorySize']) == int(systemData['Memory']['TotalSystemMemoryGB']*1024) :
	print machineDB['memorySize'],'\t\t\t\t',systemData['Memory']['TotalSystemMemoryGB']*1024,'\t\t\tMatch\t\t- Memory Size\n'
else:
	print machineDB['memorySize'],'\t\t\t\t',systemData['Memory']['TotalSystemMemoryGB']*1024,'\t\t\tMatch FAILED\t- Memory Size\n'


#print   "\n\n"
#print   "assetTag: "
#print   "comments: "
#print   "consoleHostName: "
#print   "macAddrConsole: {}".format(ethernetData['Items'][0]['FactoryMacAddress'])
#print machineDB[macAddrConsole]
#print ethernetData['Items'][0]['FactoryMacAddress']
#print   "consoleServer: "
#print   "consoleServerPort: "
#print   "cpuCount: {}".format(systemData['ProcessorSummary']['Count'])
#print   "cpuSpeed: "
#print   "datacenter: "
#print   "defaultRoute: "
#print   "dnsDomain: "
#print   "hardwareType: "
#print   "arch: "
#print   "hardwareVendor: "
#print   "hostname: "
#print   "ipAddr: "
#print   "ipAddrSecondary: "
#print   "lastUpdated: "
#print   "macAddr: {}".format(networkAdapters['PhysicalPorts'][0]['MacAddress'])
#print   "macAddrSecondary: {}".format(networkAdapters['PhysicalPorts'][1]['MacAddress'])
#print   "macAddrTernary: "
#print   "macAddrQuadrary: "
#print   "maintenance: "
#print   "memorySize: {}".format(systemData['Memory']['TotalSystemMemoryGB']*1024)
#print   "netmask: "
#print   "networkSwitch: "
#print   "networkSwitchPort: "
#print   "networkSwitchPortSecondary: "
#print   "networkSwitchSecondary: "
#print   "os: "
#print   "osPatchLevel: "
#print   "osVersion: "
#print   "owner: "
#print   "ownerTMID: "
#print   "providesServices: "
#print   "rackNumber: "
#print   "rackPorts: "
#print   "rackPosition: "
#print   "serialNumber: {}".format(systemData['SerialNumber'])
#print   "cageNumber: "
#print   "status: "

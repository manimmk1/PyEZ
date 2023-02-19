"""
Program to connect to Juniper router and get show version details
"""

from jnpr.junos import Device
import json
from getpass import getpass

print ("This is a py script to connect to Junos")

juser = input("Enter username: ")
jpasswd = getpass("Enter password: ")

connection = Device(host='192.168.122.2', user=juser, password=jpasswd)

connection.open()
print ('connection status is : ', connection.connected)

version = connection.rpc.get_software_information({'format': 'json'})

with open ('version.json', 'w') as wf:
 json.dump(version, wf)

with open ('version-i2.json', 'w') as wf:
 json.dump(version, wf, indent=2)

print ("Junos version is: ", version['software-information'][0]['junos-version'][0]['data'])

connection.close()
print ('connection status is : ', connection.connected)


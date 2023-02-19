"""
Program to connect to Juniper router and get show interface details
"""

from jnpr.junos import Device
import json
from getpass import getpass

print ("This is a py script to connect to Junos")

juser = input("Enter username: ")
jpasswd = getpass("Enter password: ")

connection = Device(host='x.x.x.x', user=juser, password=jpasswd)

connection.open()
print ('connection status is : ', connection.connected)

intf = connection.rpc.get_interface_information({'format': 'json'})

with open ('../data/interface.json', 'w') as wf:
 json.dump(intf, wf)

with open ('../data/interface-terse.json', 'w') as wf:
 json.dump(terse, wf)

connection.close()
print ('connection status is : ', connection.connected)


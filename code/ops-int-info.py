"""
Program to connect to Juniper router and get show interface details
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

intf = connection.rpc.get_interface_information({'format': 'json'})

terse = connection.rpc.get_interface_information({'format': 'json'}, terse=True)

ge001 = connection.rpc.get_interface_information({'format': 'json'}, interface_name='ge-0/0/1.0')


with open ('interface.json', 'w') as wf:
 json.dump(intf, wf)

with open ('interface-terse.json', 'w') as wf:
 json.dump(terse, wf)

with open ('interface-ge001.json', 'w') as wf:
 json.dump(ge001, wf)

with open ('interface-i2.json', 'w') as wf:
 json.dump(intf, wf, indent=2)

with open ('interface-terse-i2.json', 'w') as wf:
 json.dump(terse, wf, indent=2)

with open ('interface-ge001-i2.json', 'w') as wf:
 json.dump(ge001, wf, indent=2)

connection.close()
print ('connection status is : ', connection.connected)


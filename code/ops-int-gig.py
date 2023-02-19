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

ge001 = connection.rpc.get_interface_information({'format': 'json'}, interface_name='ge-0/0/1.0')


with open ('../data/interface-ge001.json', 'w') as wf:
 json.dump(ge001, wf)

with open ('../data/interface-ge001-i2.json', 'w') as wf:
 json.dump(ge001, wf, indent=2)

connection.close()
print ('connection status is : ', connection.connected)


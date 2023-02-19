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

terse = connection.rpc.get_interface_information({'format': 'json'}, terse=True)

with open ('../data/interface-terse.json', 'w') as wf:
 json.dump(terse, wf)

with open ('../data/interface-terse-i2.json', 'w') as wf:
 json.dump(terse, wf, indent=2)

connection.close()
print ('connection status is : ', connection.connected)


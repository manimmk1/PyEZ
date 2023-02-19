"""
Program to connect to Juniper router and get show route details
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

route = connection.rpc.get_route_information({'format': 'json'})

with open ('../data/route.json', 'w') as wf:
 json.dump(route, wf)

with open ('../data/route-i2.json', 'w') as wf:
 json.dump(route, wf, indent=2)

connection.close()
print ('connection status is : ', connection.connected)


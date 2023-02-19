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

route_dst = connection.rpc.get_route_information({'format': 'json'}, destination='x.x.x.x')

with open ('../data/route-dst.json', 'w') as wf:
 json.dump(route_dst, wf)

with open ('../data/route-dst-i2.json', 'w') as wf:
 json.dump(route_dst, wf, indent=2)

connection.close()
print ('connection status is : ', connection.connected)


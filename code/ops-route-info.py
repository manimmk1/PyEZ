"""
Program to connect to Juniper router and get show route details
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

route = connection.rpc.get_route_information({'format': 'json'})

route_dst = connection.rpc.get_route_information({'format': 'json'}, destination='192.168.122.2')

with open ('route.json', 'w') as wf:
 json.dump(route, wf)

with open ('route-i2.json', 'w') as wf:
 json.dump(route, wf, indent=2)

with open ('route-dst.json', 'w') as wf:
 json.dump(route_dst, wf)

with open ('route-dst-i2.json', 'w') as wf:
 json.dump(route_dst, wf, indent=2)

connection.close()
print ('connection status is : ', connection.connected)


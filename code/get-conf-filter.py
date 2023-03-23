"""
This is a python program to get config from junos
"""

from jnpr.junos import Device
from getpass import getpass
from lxml import etree
import json

print ('Program to get config from junos')

juser = input ('Enter username: ')
jpass = getpass('Enter password: ')

conn = Device(host='x.x.x.x', user=juser, password=jpass)

try:
 conn.open()

except: 
 print('connection to junos cannot be established')

else: 
 if conn.connected == True: 
  print ('Connection established') 

 filter=etree.XML('<system><services/></system>')
 filter1='<system><services/></system>'

 jconf_srv_var = conn.rpc.get_config(filter_xml=filter1, options={'format': 'set'})

 jconf_srv_fo = open('../data/conf_srv', 'w')
 print (etree.tostring(jconf_srv_var, encoding='unicode', pretty_print=True), file=jconf_srv_fo)
 jconf_srv_fo.close()

 conn.close()
 if (conn.connected == False): 
  print ('connection closed')


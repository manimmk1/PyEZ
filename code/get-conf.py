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

 jconf_native_var = conn.rpc.get_config()

 jconf_native_fo = open('../data/conf_native', 'w')
 print (etree.tostring(jconf_native_var, encoding='unicode', pretty_print=True), file=jconf_native_fo)
 jconf_native_fo.close()

 conn.close()
 if (conn.connected == False): 
  print ('connection closed')


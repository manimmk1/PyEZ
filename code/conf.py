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
conn.open()

if conn.connected == True: 
 print ('Connection established') 

filter=etree.XML('<system><services/></system>')
filter1='<system><services/></system>'

jconf_native_var = conn.rpc.get_config()

jconf_set_var = conn.rpc.get_config(options={'format': 'set'})

jconf_srv_var = conn.rpc.get_config(filter_xml=filter1, options={'format': 'set'})

jconf_native_fo = open('conf_native', 'w')
print (etree.tostring(jconf_native_var, encoding='unicode', pretty_print=True), file=jconf_native_fo)
jconf_native_fo.close()

jconf_set_fo = open('conf_set', 'w')
print (etree.tostring(jconf_set_var, encoding='unicode', pretty_print=True), file=jconf_set_fo)
jconf_set_fo.close()

jconf_srv_fo = open('conf_srv', 'w')
print (etree.tostring(jconf_srv_var, encoding='unicode', pretty_print=True), file=jconf_srv_fo)
jconf_srv_fo.close()


conn.close()

if (conn.connected == False): 
 print ('connection closed')



SETUP PyEZ: 

INSTALL PYTHON3 / PIP3 PACKAGES
apt-get install python3-pip
pip3 install junos-eznc


SET HOSTNAME AND CREATE USERS
set system host-name vMX
set system login user auto uid 2000
set system login user auto class operator
set system login user auto authentication plain-text-password <password>
set system root-authentication plain-text-password <password>

  
ENABLE SSH & NETCONF
set system services ssh
set system services netconf ssh

  
IMPORT REQUIRED MODULES 
from jnpr.junos import Device


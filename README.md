
SETUP PyEZ: 
1. Install python3 / pip3 packages
2. Set hostname and create users
3. Enable ssh & Netconf on juniper
4. Under Python import required modules


1. Install python3 / pip3 packages
  apt-get install python3-pip : to install pip
  pip3 install junos-eznc : to install a python package
  

2. Set hostname and create users
  set system host-name vMX
  set system login user auto uid 2000
  set system login user auto class operator
  set system login user auto authentication plain-text-password <password>
  set system root-authentication plain-text-password <password>

3. Enable ssh & Netconf on juniper
  set system services ssh
  set system services netconf ssh

4. Under Python import required modules 
  from jnpr.junos import Device


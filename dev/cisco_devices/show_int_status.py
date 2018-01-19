#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

ip_addr = raw_input("Enter IP Address: ").strip()
password = getpass()

cisco = {
    'device_type': 'cisco_ios',
    'ip': ip_addr,
    'username': 'pyclass',
    'password': password,
    'port': 22,
    'ssh_config_file': '~/.ssh/config',
    'verbose': False,
}

net_connect = ConnectHandler(**cisco)
output = net_connect.send_command('show users')
print output
print
print net_connect.find_prompt()
print 

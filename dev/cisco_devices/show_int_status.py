
# URL: https://pynet.twb-tech.com/blog/automation/netmiko-proxy.html
#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass


def cisco_output_to_file():
    f = open('cisco.txt', 'w')
    f.write(cisco_output)
    f.close()

openNewFile = cisco_output_to_file()

# prompt the user to enter an ip address
ip_addr = input("Enter IP Address: ").strip()

# prompt the user for the password for that IP (above)
password = getpass()

cisco = {
    'device_type': 'cisco_ios',
    'ip': ip_addr,
    'username': 'rdiaz',
    'password': password,
    'port': 22,
    'ssh_config_file': '~/.ssh/config',
    'verbose': False,
}

# Connects to ip_addr referanced in the cisco dictionary and uses the password also found on the dictionary
net_connect = ConnectHandler(**cisco)

# Creates a var that is the output/result of (connecting to the device via ssh, and the commands that are send)
cisco_output = net_connect.send_command('show int status')

# Print output of the cisco output on the terminal
#print (output)

print (openNewFile)

print
print (net_connect.find_prompt())
print

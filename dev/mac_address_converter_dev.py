# By: Ricardo Diaz
# Date: 20171224
# Python3.6
# Name: mac_address_converter.py

import re

# Functions
def windowsMacDef():
    print ("testing windows function")

def linuxMacDef():
    print ("testing linux function")

def ciscoMacDef():
    print ("testing cisco function")

def userMacDef():
    print ("testing user function")

# Explaining the purpose of the program
print ("\n# READ ME")
print ("Purpose of this program is to convert any mac address (regardless of format) and convert it to a specific vendor mac address format")

# Examples/list of mac address formats
print ("\n# MAC address format examples per vendor\nw. D8-FC-93-7B-67-7C - Windows\nl. 8c:85:90:1a:87:c5 - Linux\nc. d8fc.937b.677c - Cisco\nu. D8FC937B677C or d8fc937b677c - Manual User\n")

# User input | desired mac address output
userLetterSelection = input("From the above list, please select the desired MAC address output: ")
print ("[" + userLetterSelection + "] is what you have selected")

# User input | enter mac address in any format
#userMacAdd = input ("Enter MAC address(regardless of format): ")
#TEST print (userMacAdd)


# If statements
if userLetterSelection in ['w', 'W']:
    print ("You have selected Windows")
    windowsMacDef()
elif userLetterSelection in ['l', 'L']:
    print ("You have selected Linux")
    linuxMacDef()
elif userLetterSelection in ['c', 'C']:
    print ("You have selected Cisco")
    ciscoMacDef()
elif userLetterSelection in ['u', 'U']:
    print ("You have selected Manual")
else:
    print ("INVALID SELECTION")

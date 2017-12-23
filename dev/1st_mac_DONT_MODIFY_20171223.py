
import re

# By: Ricardo Diaz
# Update: 20171223
# Python 3.6

# Prompt the user to enter a windows format mac address | D8-FC-93-7B-67-7C  | Ricardo Wireless mac address
print ("\n" + "===" * 4)
userWindowsMacAdd = input("Enter Windows MAC address to convert to a Cisco MAC address format\nExample: A1-B2-C3-D4-E5-F6 should be a1b2.c3d4.e5f6\nMac address: ")
print ("===" * 4)

# Explaining what the program will do
print("\nConverting [" + userWindowsMacAdd + "] into a cisco mac address format. (example: abcd.eff1.42ab)")

# Windows Mac address to Regex output
RegWindowsMacAdd = (re.findall(r'[0-9,A-Z].',userWindowsMacAdd))

# Printing the regex output (in an array/list)
print(RegWindowsMacAdd)

# Converting Regex output [RegWindowsMacAdd] into lowercase string so we can later slice the 12 characters into 3 parts
str_winRegMacAdd = "".join(RegWindowsMacAdd)
print ("\nConverting Regex output [RegWindowsMacAdd] into lowercase string\nLowercase mac address: " + str_winRegMacAdd.lower())

# Create variables for each individual group (i.e mac add = 1234.5678.90ab | 1234 - group 1 | 5678 - group 2 |.. etc )
mac_group_1 = (str_winRegMacAdd[:4].lower())
mac_group_2 = (str_winRegMacAdd[4:8].lower())
mac_group_3 = (str_winRegMacAdd[8:12].lower())

# Putting it all together by connecting the mac address groups with a "."
print ("\n" + "===" * 4)
print("Below is the Cisco MAC address format")
print (mac_group_1 + "." + mac_group_2 + "." + mac_group_3)
print ("===" * 4)

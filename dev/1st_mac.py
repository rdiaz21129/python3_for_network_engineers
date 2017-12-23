
import re

# D8-FC-93-7B-67-7C  | Ricardo Wireless mac address

userWindowsMacAdd = input("Enter Windows MAC address: ")
print("Converting [" + userWindowsMacAdd + "] into a cisco mac address format. (i.e. abcd.eff1.42ab)")

# Windows Mac address to Regex output
RegWindowsMacAdd = (re.findall(r'[0-9,A-Z].',userWindowsMacAdd))
# print(RegWindowsMacAdd)



"""
windowsMacAdd = ("AB-23-CE-24-7A-B8")
print ("Windows MAC address is --> " + windowsMacAdd)

# Regex
RegMacAdd = (re.findall(r'[0-9,A-Z].',windowsMacAdd))
print (RegMacAdd)

# Converting Regex output (list/array) to a string
str_RegMacAdd = "".join(RegMacAdd)
print ("Converting regex output to a string --> " + str_RegMacAdd)

# Converting into cisco mac address format + lowercase
#print ("cisco mac address format: ") + (str_RegMacAdd[:4].lower()) + (".") + (str_RegMacAdd[4:8].lower()) + (".") + (str_RegMacAdd[8:12].lower())
print("cisco mac address format: " + str_RegMacAdd[:4].lower() + "." + str_RegMacAdd[4:8].lower() + "." + str_RegMacAdd[8:12].lower())
print("##" * 12)
"""


'''
print
print ("=== DEV AREA ===")
print ("==" * 10)
str_mac_add = "123456789012"
print ("string mac address is --->" + str_mac_add)
# Slicing the Mac address
print ("Slicing str_mac_add / 123456789012")
print (str_mac_add[:4])
print (str_mac_add[4:8])
print (str_mac_add[8:12])
print ("Cisco MAC Address format --> ") + (str_mac_add[:4]) + (".") + (str_mac_add[4:8]) + (".") + (str_mac_add[8:12])
#print ("cisco mac format ---> " + str_mac_add[:4] + "." + str_mac_add[4:8] + "." str_mac_add[8:12])
print ("==" * 10)
'''

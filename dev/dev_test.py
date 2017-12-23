# Dev Area

firstName = input ("what is your name? : ")
print ("Hello " + firstName + ", this is a dev area")
print ("python 3 works")

print ("This is the first line\nThis is the second line")



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

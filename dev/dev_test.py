# Dev Area


user_ip_address_list = [] #Create empty list
list_counter = 0

while 1 > 0:
    user_ip_address = input ("\nEnter ip address or starting octet that you want to EXCLUDE from the search: ")

    if len(user_ip_address) <= 0:
        print ("\n**You entered something that is less than zero**")
        print ("Number of times you entered something: ", list_counter, "\n")
        print ("list: ", user_ip_address_list) # print list when complete
        break #STOP THE WHILE LOOP

    else:
        user_ip_address_list.insert(list_counter, user_ip_address) # adding to list
        list_counter = list_counter + 1
        print ("Adding [",user_ip_address,"] to list\n")







"""
def main():
    # read file
    file = open("sample_txt_file", "r")
    lines = file.readlines()
    file.close()

    # look for patterns
    countYES = 0
    countNO = 0
    countRicardo_lucy = 0
    for line in lines:
        line = line.strip()
        #print (line)
        if line.find("Ricardo") != -1 and len(line) ==7:
            countRicardo_lucy = countRicardo_lucy + 1
            print (line)


    print ("\nRicardo and lucy count: ", countRicardo_lucy, "\n")

        #if line.find("YES") != -1:
            #countYES = countYES + 1
            #print (line)
        #if line.find("NO") != -1:
            #countNO = countNO + 1


    #print ("Yes: ", countYES)
    #print ("NO: ", countNO)

#main()

#y = 10
#x = input("enter a number that you would like to get added by 10: ")

#print (y + int(x))



#testMath()

'''

def testFunction():
    print ("testing function")

testFunction()

userLetter = input("Type in a letter: ")
print ("The letter that you entred was: [" + userLetter + "]\n")

if userLetter in ['r', 'R']:
    print ("Ricardo starts with the letter [R]")
elif userLetter in ['i', 'I']:
    print ("India starts with the letter [I]")
else:
    print ("You entered a letter that sucks\n")


firstName = input ("what is your name? : ")
print ("Hello " + firstName + ", this is a dev area")
print ("python 3 works")

print ("This is the first line\nThis is the second line")

print ("adskfljdsaf")


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
"""

# Ricardo Diaz
# 20170120
# Python 3.6
# Purpose: Parse cisco syslog messages/ACL logs. Functions include excluding or including ip addresses

# Import mondules
import re,sys

# Define Function
def exclude_ip():

    # OPEN/CLOSE SYSLOG FILE
    # Opens the file "syslog_data_1" in read mode "r"
    syslog_data_file = open("syslog_data_real", "r")

    # Sends output of open file to a variable called = switch_config_fileOutput
    syslog_data_fileOutput = syslog_data_file.readlines()

    # Close file
    syslog_data_file.close()


    # Variables for the below while loop | Asks the user to ip addresses or start of prifix
    user_ip_address_list = [] #Created empty list that will get populated
    list_counter = 0 #variable that will be used in the below while loop

    while 1 > 0:
        user_ip_address = input ("\n(enter nothing to exit)\nEnter ip address or starting octet that you want to EXCLUDE from the search: ")

        # stop/brake while loop condition
        if len(user_ip_address) <= 0:
            print ("\n**You entered something that is less than zero**")
            print ("Number of times you entered something: ", list_counter, "\n")
            print ("complete list: ", user_ip_address_list) # print list when complete
            break #STOP THE WHILE LOOP

        else:
            user_ip_address_list.insert(list_counter, user_ip_address) # adding to list
            list_counter = list_counter + 1
            print ("Adding [",user_ip_address,"] to list\n")


    # 3.
    # counters
    count_ip_address = 0
    x = 0

    # get count of items/values in list/array, staring at 1
    lenOfuser_ip_address_list = len(user_ip_address_list)



    print ("LEN OF USER INPUT LIST: ", lenOfuser_ip_address_list)
    #print ("**TEST** PRINTING user_ip_address_list index 0", user_ip_address_list[0])
    #print (user_ip_address_list[0]) # should print first user input
    for ip_addresses in syslog_data_fileOutput:
        ip_addresses = ip_addresses.strip()  # remove any blank lines
        x = x+1
#### TypeError: must be str, not list ####
        # find, if the string is in the file == 0 IF NOT == -1
        if ip_addresses.find(user_ip_address_list[x]) != -1:
            #print(ip_address)
            count_ip_address = count_ip_address + 1
        else:
            print (ip_addresses)
    print ("\nIP address [", user_ip_address, "] showed up: [", count_ip_address,  "] times and was not printed")




# Call function
exclude_ip()

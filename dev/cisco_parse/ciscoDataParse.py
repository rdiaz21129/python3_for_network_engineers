# Ricardo Diaz
# 20170115
# Python 3.6
# Purpose: Parse cisco syslog messages/ACL logs. Functions include excluding or including ip addresses

# Import mondules
import re,sys

# Define Function
def exclude_ip():

    # Variables for the below while loop
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

    # OPEN/CLOSE SYSLOG FILE
    # Opens the file "syslog_data_1" in read mode "r"
    syslog_data_file = open("syslog_data_real", "r")

    # Sends output of open file to a variable called = switch_config_fileOutput
    syslog_data_fileOutput = syslog_data_file.readlines()

    # Close file
    syslog_data_file.close()


    # counters
    count_ip_address = 0

    #print (switch_config_fileOutput)
    for ip_address in syslog_data_fileOutput:
        ip_address = ip_address.strip()  # remove any blank lines

#### TypeError: must be str, not list ####
        # find, if the string is in the file == 0 IF NOT == -1
        print (user_ip_address_list)
        if ip_address.find(user_ip_address_list) != -1:
            #print(ip_address)
            count_ip_address = count_ip_address + 1
        else:
            print (ip_address)
    print ("\nIP address [", user_ip_address, "] showed up: [", count_ip_address,  "] times and was not printed")




# Call function
exclude_ip()

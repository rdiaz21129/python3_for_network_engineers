# Ricardo Diaz
# 20170113
# Python 3.6

# Import mondules
import re,sys

#ip_address = input ("Enter IP address: ")
#print(ip_address)

def exclude_ip():
    print ("\nEnter ip address or starting octet that you want to EXCLUDE from the search")
    #user_ip_address = input ("Enter IP address: ") # IP address we want to search
    user_ip_address = []

## WORK ON THIS!!!!!
    while True:
        user_ip_address = input ("Enter ip address or starting octet that you want to EXCLUDE from the search")
        if user_ip_address.len() < 0:
            break

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

        # find, if the string is in the file == 0 IF NOT == -1
        if ip_address.find(user_ip_address) != -1:
            #print(ip_address)
            count_ip_address = count_ip_address + 1
        else:
            print (ip_address)
    print ("\nIP address [", user_ip_address, "] showed up: [", count_ip_address,  "] times and was not printed")





exclude_ip()

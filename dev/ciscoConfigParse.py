# Ricardo Diaz
# 20170108
# Python 3.6

# Import mondules
import re,sys

# Opens the file "ex_switch_config" in read mode "r"
switch_config_file = open("ex_switch_config", "r")

# Sends output of open file to a variable called = switch_config_fileOutput
switch_config_fileOutput = switch_config_file.readlines()

#print (switch_config_fileOutput)
for x in switch_config_fileOutput:
    #TESTprint (x)
    if ['address'] in switch_config_fileOutput:
        print (x)

# Close file
switch_config_file.close()

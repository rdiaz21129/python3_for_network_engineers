# Ricardo Diaz
# 20170108
# Python 3.6

# Import mondules
import re,sys

# Opens the file "ex_switch_config" in read mode "r"
switch_config_file = open("ex_switch_config", "r")

# Sends output of open file to a variable called = switch_config_fileOutput
switch_config_fileOutput = switch_config_file.read()
switch_config_file.close()

print (switch_config_fileOutput)

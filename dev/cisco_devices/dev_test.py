
#https://stackoverflow.com/questions/8583615/how-to-check-if-a-line-has-one-of-the-strings-in-a-list
#https://stackoverflow.com/questions/29106881/check-if-any-of-the-items-of-a-list-is-in-a-line-of-a-file-if-not-then-write-t





# OPen and close file
f = open('serial_numbers.txt', 'r')
f_output = f.readlines()
f.close()

# Create lists that will be used in for loops
x = ['pizza', 'tacos', 'beer']

# For variable in f_output
for line in f_output:
    line = line.strip() # remove blank lines

    if any(newvar in line for newvar in x):
        print (line)

'''
food = ("pizza")

f = open("createdFile.txt", "w")
f.write("hello,\nopening file and closing it\n")
f.close()
'''

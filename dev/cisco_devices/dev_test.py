
f = open('serial_numbers.txt', 'r')
f_output = f.readlines()
f.close()

#print (f_output)
x = ('FDO1441P0CR')
x_list = ['xxricardo', 'carlosxxx', 'lucero']
for line in f_output:
    line = line.strip() # remove blank lines
    #print (line)
    for x_list in line:
        print (x_list)

'''
food = ("pizza")

f = open("createdFile.txt", "w")
f.write("hello,\nopening file and closing it\n")
f.close()
'''

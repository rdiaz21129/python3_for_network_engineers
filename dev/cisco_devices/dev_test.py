
#https://stackoverflow.com/questions/8583615/how-to-check-if-a-line-has-one-of-the-strings-in-a-list
#https://stackoverflow.com/questions/29106881/check-if-any-of-the-items-of-a-list-is-in-a-line-of-a-file-if-not-then-write-t
my_unwanted_words = set(['ssh', 'snmp', 'etc'])
with open("infile_test.txt", 'r') as infile, open("newfile.txt", 'w') as newopen:
    lines = infile.readlines()
    [newopen.write(line) for line in lines if not (set(line.split()) & my_unwanted_words)]




'''
f = open('serial_numbers.txt', 'r')
f_output = f.readlines()
f.close()

#print (f_output)
name = ('ricardo')
x = ['pizza', 'tacos', 'beer']
for line in f_output:
    line = line.strip() # remove blank lines
    #print (line)
    if x in line:
        print (x)


food = ("pizza")

f = open("createdFile.txt", "w")
f.write("hello,\nopening file and closing it\n")
f.close()
'''

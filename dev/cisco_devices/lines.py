
#prompt the user for number, number of lines that will be created in a file
user_range_input = int(input("Enter number of lines you want created: "))

# Define function that will create lines
# 1
def createLines(y):
    x_count = 0
    for i in range(y):
        x_count+=1
        print ("This is line", x_count)
        

functionOneOutput = createLines

#print ("***" * 8)

#print (functionOneOutput(user_range_input))
#'''
f = open("createdFile.txt", "w")
f.write(str(functionOneOutput(user_range_input)))
f.close()
#'''

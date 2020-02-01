
file = open("../testData/demo.txt",'a')
file.write("Hello all \n")
# file.newlines()
file.write("\nSelenium Python jobs")
file.close()

f = open("../testData/demo.txt",'r')
for x in f:
    print(x)



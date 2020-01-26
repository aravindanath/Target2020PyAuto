#
# try:
#     car = {"make": "bmw", "Model": '550i', 'year': 2019}
#     print(car["colour"])
# except:
#     print("Error")
#     raise
#


print("Starting....")

print("DB connction is open...")
try:
    # a = 10
    # b = 0
    # print(a / b)

    read = open("./drive/text.txt",'r')
    read.readline()
except ZeroDivisionError:

    print("Zero division error")
    raise Exception("Zero division error")
#     Raise is used to print the stack trace / logs
except FileNotFoundError:
    print("File not found..")
    raise Exception("File not found error")

finally:
    print("DB connction is closed...")


print("Ending....")
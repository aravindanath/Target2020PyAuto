
# https://docs.python.org/3/library/exceptions.html

print("StART...")

try:
    o =open("../drvier/demo.txt",'w')
    o.write("hello")

except  :
    print("File handled")


finally:
    print("Always executes....")


print("ending")
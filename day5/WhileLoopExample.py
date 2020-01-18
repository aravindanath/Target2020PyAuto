#
# for r in list(range(1,5)):
#     print(r)

empty=[]
print(type(empty))
print("Before appending List",empty)
x = 1
while x<10:
    empty.append(x)
    print("Hi")
    x=x+1
else:
    print(" this is else")

print("After appending List",empty)
print("Out of loop")



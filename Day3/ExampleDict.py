dict = {"door":"4"}

print(type(dict))
print(dict)

dict["model"]="2019"
dict["colour"]="White"

print(dict.keys())
print(dict.values())


for c in dict.items():
    print(c)

print(dict)

emp ={}
print("Before:",emp)
emp=dict.copy()
print("After",emp)


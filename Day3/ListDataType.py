names = ["Nazreen","Bhavya","Arvind"]
print(type(names))

print(names[2])
names.append("Hema")
print(names)
names.insert(0,"Shalu")
print(names)
names.append("Arvind")
print(names.count("Arvind"))
print("Before sort",names)
names.sort()
print("After sort",names)
names.sort(reverse=True)
print("After Reverse sort",names)
print(names[0:2])
print(names[::-1])

print(len(names))

l1 =[]
l1=names.copy()
print(l1)



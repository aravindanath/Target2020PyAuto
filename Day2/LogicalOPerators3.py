"""
and
or
is
==
 <
 >
 <=
 >=
 not
"""

a = 10
b = 20

print(a is b)
print(a == b)

print(a  < b )
print(a>b)
print(a<=b)
print(a>=b)


age  = 19
nat = "indian"
voter = True
aadhar = True

if(age >= 18 and nat is "indian" and voter and aadhar):

    print("u can vote")
else:
    print("u can not vote")
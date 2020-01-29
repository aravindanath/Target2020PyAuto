car={"Make":"kia","model":"carnival","year":2020}
try:
    print(car["colour"])
except:
    print(car["Make"])
finally:
    print("exception is handled")

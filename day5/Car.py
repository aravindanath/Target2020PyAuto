
class Cars(object):

    def __init__(self):
        print("I am special method")

    def doors(self,door):
        print("Total no of doors",door)

    city="BangAloRe"

    def make(self):
        print("2020")

class _3m(Cars):

    def windsheld(self):
        print("3m windsheld")


class BMW(_3m):

    def bmwModel(self):
        print("Bmw i500")

# Class object
# d = Cars()
# d.doors(5)
# # d.make()
# # print(d.city.replace("a","A"))
# b  = BMW();
# b.bmwModel()
# b.make()
# b.city
# b.windsheld()


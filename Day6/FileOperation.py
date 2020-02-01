
from Day6 import BaseClass

val =BaseClass.readINI("../testData/data.ini","Tc001","url")
print(val)

BaseClass.writeINI("../testData/data.ini","a","Tc001","nwURl","https://www.flipkart.com")
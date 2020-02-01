car = {'make':15,'model':'kia','year':2020}
try:
    print(car['model'])
    print(car['color'])

except ImportError:
    print("not an import error")
except:
    print("color is not a part of car")

finally:
    print("please add the element color in car")


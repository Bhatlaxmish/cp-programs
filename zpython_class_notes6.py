import datetime
import pytz
a = 3
b = 3
print(a+b)
print(a.__add__(b))  # this also does same as '+'


# object oriented
class kettel(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kow = kettel('woefrj', 234)
print(kow.make)
print(kow.price)
kow.price = 1234
print(kow.price)
hamilton = kettel("sofwe", 808)
print("modurle{}={} ,{}={}".format(
    kow.make, kow.price, hamilton.make, hamilton.price))
# class :tamplate for creating objects all objects created using the same class will have same characteristics
# object : an instance of a class
# instantiate: create an instance of a class
# method : a function defined in class
# attribution:a variable bound to an instance of a class


print(kow.__dict__)  # makes all elemetn in class as dictionary


class Acount:  # make first letter capital
    def __init__(self, name, valance):
        self.name = name
        self.valance = valance

    @staticmethod  # its a static method  no need to use self in function
    def funciotn():
        ine = 4+3
        print("finctioon is ")


if __name__ == '__main__':
    weo = Acount("sldf", 230)
    Acount.funciotn()
    print(weo.name)

class Parent:
    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    def show(self):
        print('this is in childs class')

son = Child(100)
print(son.get_num())
son.show()


#METHOD OVERRIDING 
class Phone:
    def __init__(self,price,brand,camer):
        self.price = price
        self.brand = brand
        self.camera = camer

    def buy(self):
        print("buying a phone")

class Smartphone(Phone):
    def buy(self):
        print("buying a smartphione")

s= Smartphone(200000,'Apple',13)
s.buy() ##similar to constructor overriding if both child and parents have the same methods then the method of child gets called if the class of 
#child is called
class Phone:
    def __init__(self,price,brand,camera):
        print('INSIDE PHONE CONSTRUCTOR')
        self.__price = price
        self.brand = brand
        self.camera = camera

class Smartphone(Phone):
    def __init__(self,price ,brand,camera,os,ram):
        print('Inside smartphone constructor')
        super().__init__(price,brand,camera) ##triggering super method 
        self.os = os
        self.ram = ram
        print('Inside smartphone constructor')

s = Smartphone(20000,'Samsung',12,'Android',2)

#super cannot call methods from parent class
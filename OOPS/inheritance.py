"""inheritance : 
 classes which inherit each other. two classes parent class and child class, child class ka object can easily use parent class ka data#
"""
 # DRY --- DONT REPEAT YOURSELF 
"""THATS THE CORE OF INHERITANCE FOR EG: 
IN A WEBSITE LIKE UDEMY BOTH STUDENT AND TEACHER WOULD LOGIN AND REGISTER SO INSTEAD OF CREATING SAME SET OF CODES IN CLASS 
OF STUDENT AND TEACHER WE CREATE A PARENT CODE OF LGIN AND REGISTER AND CONNECT IT WITH THESE CLASSES
"""

class user:
    def __init__(self):
        self.name = 'mudit'

    def login(self):
        print('login')

class Student(user):
    # def __init__(self):
    #     self.rollnum = '110'
    # while using inheritance we can never have constructor in te childs object wheen the 
    #parents object has a constructor as the parents constructor wont be called if there is a constructor there itself in childs class
    #child class cant access pvt members of the class 

    def enroll(self):
        print('PLEASE ENROLL IN THE BATCH')

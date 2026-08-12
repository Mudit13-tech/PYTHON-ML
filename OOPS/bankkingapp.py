#pascal case : HelloWorld,AtmBanking
#two types of classes : built-in and user defined
class Atm: 
    #static variable is defined outside class.
    __counter = 1

    #constructor: a function inside a class; used to create a variable inside a class;
    #superpower-> special function. to execute it its not needed to call the function explicitly
    #everytime an object of this class is called the constructor i =s executed always whether its called or not
    def __init__(self):
        self.pin = ' '
        self.__balance = 0 #the variable will always have a .self prefix
        self.cid = Atm.counter
        Atm.counter = Atm.counter + 1
        self.menu()

    @staticmethod 
    def get_counter():
        return Atm.__counter

    def get_balance(self):
        return self.__balance

    def menu(self):
        user_input = input("""   
        Hi how can I help you?
        1. PRESS 1 TO CREATE PIN.
        2. PRESS 2 TO CHANGE PIN.
        3. PRESS 3 TO CHECK BALANCE.
        4. PRESS 4 TO WITHDRAW.
        5. ANYTHING ELSE TO EXIT.
        """)

        if user_input == '1':
            #create pin
            self.create_pin()
            self.menu()
        elif user_input == '2' :
            #change pin
            self.change_pin()
            self.menu()
        elif user_input == '3' :
            #change balance
            self.check_balance()
            self.menu()
        elif user_input == '4' :
            # withdraw
            self.withdraw()
            self.menu()
        else : 
            exit()

    def create_pin(self):
        user_pin = int(input("ENTER YOUR PIN : "))
        self.pin = user_pin

        print('PIN CREATED SUCCESSFULLY')

        user_balance = int(input("ENTER YOUR BALANCE : "))
        self.__balance = user_balance

    def change_pin(self):
        user_oldpin = int(input("ENTER YOUR CURRENT PIN : "))
        if(user_oldpin == self.pin):
            user_pin = int(input('ENTER YOUR NEW PIN : '))
            self.pin = user_pin

            print(" NEW PIN SAVED")
        else:
            print('PIN INCORRECT !! \n TRY AGAINNN ')

    def check_balance(self):
        user_pin = int(input("ENTER YOUR PIN : "))
        if(user_pin == self.pin):
            print("YOUR BALANCE IS ",self.__balance)
        else:
            print(" INCORRECT PIN")

    def withdraw(self):
        user_pin = int(input("ENTER YOUR PIN : "))
        if(user_pin == self.pin):
            print(" YOUR BALANCE IS ",self.__balance)
            withdrawal_Amt = int(input('ENTER THE AMOUNT YOU WANT TO WITHDRAW : '))
            if(withdrawal_Amt > self.__balance):
                print(' INSUFFICIENT FUNDS')
            else:
                self.__balance = self.__balance - withdrawal_Amt

            print(" THE CURRENT BALANCE IS : ",self.__balance)

        else:
            print('PIN INCORRECT TRY AGAIN')      
obj = Atm()


Atm.__counter()

#instance-variable : different value for each object, instance variable object ka hota h

#static-variable : same value for each object, static variable classs ka hota




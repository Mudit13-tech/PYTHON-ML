#class relationship : aggregation and inheritance
# aggregation : 
# one class owns the other class 
# you can never use private entities when using aggregation#
class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def __str__(self):
        return 'Name = {},Gender = {},City = {},Pin = {},State = {}'.format(self.name,self.gender,self.address.city,self.address.pin,self.address.state)

    def edit_details(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)


class Address:
    def __init__(self,city,pin,state):
        self.city = city
        self.pin = pin
        self.state = state

    def __str__(self):
        return 'City = {},Pin = {},State = {}'.format(self.city,self.pin,self.state)
    

    def get_city(self):
        return self.__city

    def edit_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state

add1 = Address('guwahati',781009,'assam')
cust = Customer('nitish','male',add1)
print(cust)

cust.edit_details('mudit','mumbai',111111,'maharastra')

print(cust)




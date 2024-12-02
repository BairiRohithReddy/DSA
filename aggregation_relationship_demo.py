'''
Classes majorly exhibit 2 kinds of relationships 
1. Aggregation 
2. Inheritance
'''
#Aggregation demo

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
        
    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)
        
class Address:
    
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state
        
    def change_address(self, new_city, new_pincode, new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state
        
add = Address('Nspt', 506132, 'TG')
cust = Customer('Rohith', 'Male', add)
cust.edit_profile('Pandu','Wgl', 506100, 'TG')
print(cust.address.pincode)        
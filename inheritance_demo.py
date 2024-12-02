# class User:
#     def login(self):
#         print("login")
        
#     def register(self):
#         print("register")
        

# class Student(User):
    
#     def enroll(self):
#         print("enroll")
        
#     def review(self):
#         print("review")
        
# stu1 = Student()
# stu1.enroll()
# stu1.register()
# stu1.login()
# stu1.review()

# # from this we can see that the child class Student can access all the methods or members of the parent class.
# # this is called inheritance 
# # but the inverse is not true

# u = User()
# u.login()
# u.register()
# #u.review() # this throws an error
# #u.enroll() # this throws an error as these are not a part of user class and they are also not inherited from the student class

# inheriting constructor demo

class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera
        print("inside Phone Class")
        
class Smartphone(Phone):
    pass

s = Smartphone(20000, 'Apple', 13)
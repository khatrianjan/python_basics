"""1. class and __init__"""
"""create a Book class with title,author,year of publication"""
#1. when creatind and obj ,these 3 values should be initialize using__init__
#2 then print book detai;s using a method
"""hint
use self.title,self.author, se;f.year in __Init__
create method show_detail(self)"""

# class Book:
#     def __init__(self,title,author,release_year):
#         self.title = title
#         self.author = author
#         self.release_year = release_year

#     def show_detail(self):
#         print(f"title is {self.title}")
#         print(f"author is  {self.author}")
#         print(f"date is {self.release_year}")

# detail = Book("python","von", 2018)
# detail.show_detail()

#######################################################################################
"""Encapsulation """
# class A:

#     def __init__(self):
#         self.a = 5  #public
#         self._b = "ram" #protected_
#         self.__c= "private c " #__ private
#         #python save self._A__c ="private c" => name mangling

#         """geter or seter are used for values in protected and private attr"""
#     def get_c(self):
#         return self.__c
#     """best practise"""
#     @property
#     def c(self):
#         return self.__c

# a1 = A()
# #print(a1._b)
# #print(a1.__C)  # A OBJ has no atrr --c error AttributeError
# """accesing private & protected method"""
# # print(a1._A__c)
# #print(a1.get_c())
# print(a1.c)
######################################################################
# class BankAccount:
#     def __init__(self,acc_no,first_bal = 0):
#         self.__acc_no = acc_no
#         self.__balance = first_bal

#     @property
#     def acc_no(self): #setter
#         return f"XXXXX{self.__acc_no[-4:]}"
#     @property
#     def balance(self):
#         return self.__balance
#     @property
#     def balance(self,new_bal):
#         if new_bal<=0:
#             raise Exception("deposit bal cant be less than 1000")
#         self.__balance= new_bal

# a1 =BankAccount("23123241")
# # print(a1.acc_no)
# # a1.balance = 200
# # print(a1.balance)
# try:
#     a1.balance = 2000
# except Exception as e:
#     print(e)
# finally:
#     print(a1.balance(new_bal = 500))
###################################################################################
"""inheritance"""
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         return "Animal Sound !!!"
    
# class Dog(Animal):    #Animal => superclass, Dog=>subclass
#     def speak(self):   #method overriding
#         return f"{self.name} bark !!!"
    

# d = Dog("tom")
# print(d.speak())
#############################################################################################

# class user:
#     def __init__(self,username, email):
#         self.username = username
#         self.email = email

#     def display_info(self):
#         print(f"user:{self.username},Email:{self.email}")

# #derived class
# class Customer(user):
#     def __init__(self, username, email,address):
#         super().__init__(username, email)
#         self.address = address
#     def display_info(self):
#         super().display_info()
#         print(f"address:{self.address}")

# #another derived class
# class admin(user):
#     def __init__(self, username, email,phone_no):

#         super().__init__(username, email)
#         self.phone_no = phone_no
#     def display_info(self):
#         super().display_info()
#         print(f"Address:{self.phone_no}")

# a1= admin("anjan","anjan@gmail.com","9845612955")
# a1.display_info()
    
# c1 = Customer("john","john@gmail.com","chitwan bharatpur")
# c1.display_info()
    

##################################################################################################

"""TOPIC
1. class &o obj
2. __init__ constructor
3. instance attribute and method
4. class attribute and method
5.default arugument
6.object interaction
7. Encapsulation
8. real life modeling problem"""
################################################################################
"""1.)CREATE A CLASS :APTOP
aTTRUBTE
.brand
.model
.price
methods > show_details() print all info"""

# class Laptop:
#     def __init__(self,brand, model, price):
#         self.brand= brand
#         self.model= model
#         self.price= price
    
#     def show_details(self):
#         print(f"Brand:{self.brand}")
#         print(f"MODEL: {self.model}")
#         print(f"Price: {self.price}")
    

# a = Laptop("lenovo", "notebook", 150000)
# print(a.show_details())
###########################################################################################
"""create a circle class with attr radius method area() and circumferernce()
use math.pi from math module"""
# import math
# class Circle:

#     #attribute
#     def __init__(self,radius):
#         self.radius= radius

#     #method to  calculate area
#     def area(self):
#         # return math.pi *self.radius * self.radius
#         print(math.pi *self.radius * self.radius)
    
# #method to calculate the circumference
#     def circumference(self):
#         # return  2*math.pi*self.radius 
#         print( 2*math.pi*self.radius)
    
# a = Circle(5)
# # print(a.circumference())
# # print(a.area())
# a.area()
# a.circumference()

############################################################
"""create a class Employee with class atrr company_name =TechSoft
has name position salary 
metod show_info(),change_com(cls,name) use @classmethod and cls.company_name = new_name"""
# class Employee:
#     company_name = "TechSoft"

#     def __init__(self,name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
    
#     def show_info(self):
#         print(f"name: {self.name}")
#         print(f"position:{self.position}")
#         print(f"salary:{self.salary}")
#         print(f"company: {Employee.company_name}")

#     @classmethod
#     def change_company(cls, newname):
#         cls.company_name = newname
    
# a = Employee ("ram","HR", 450000)
# a.show_info()

# print("\n after changing name.........\n")
# Employee.change_company("fantech")
# b= Employee("anjan","manager",50000)
# b.show_info()
#########################################################
"""design a class shopingCart
attr is customer name ,cart
methods add_item(item),remove_item(item),view_cart()
use self.cart=[] in __init__"""

# class ShoppingCart:
#     def __init__(self,name,):

#         self.name = name
#         self.cart = []  #initialize cart

#     def add_item(self,item):
#         #add item to cart
#         self.cart.append(item)
#         print(f"add '{item}'to{self.name}'s cart")
#     def remove_item(self,item):
#         if item in self.cart:
#             self.cart.remove(item)
#             print(f"remove '{item}'from {self.name}'s cart")
#         else:
#             print(f"'{item}' not found in {self.name}'s cart")
#     def view_cart(self):
#         #display the content
#         if self.cart:
#             print(f"{self.name}'s cart contains:")
#             for i, item in enumerate(self.cart,start= 1):
#                 print(f"{i}. {item}")
#         else:
#             print(f"{self.name}'s cart is empty.")
# a = ShoppingCart("Anjan")
# a.add_item("mouse")
# a.add_item("keyboard")
# a.view_cart()
# a.remove_item("keyboard")
# a.view_cart()
######################################################################################################
        
    
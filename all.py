

#naming convention classname create,MyDog is preferred over my_dog

"""
class MyDog:
    #constructor means the function is called when an object is created
    '''In Python, a constructor is a special method __init__() that 
    automatically runs when 
    you create a new instance of a class.
      Its primary job is to initialize the object's attributes 
      and set up its starting state'''
    def __init__(self,name):#constructor with parameter
        self.name=name #assigning value

    def show_name(self):
        print("my dog name is: ",self.name)
x= MyDog('puntey')   #create an object
x.show_name()#call the function of the object x
"""
'''
class Robot:
    #constructor defining with name value
    def __init__(self,name,age,colour):
        self.name=name
        self.age=age
        self.colour=colour
    def show_name(self):
        print("my robot name is: ",self.name)
    def show_age(self):
        print("my robot age is: ",self.age)
    def show_colour(self):
        print("my robot colour is: ",self.colour)

#create an object using classname and parameter
nam=Robot('puntey',24,'white')
nam.show_age()
'''

#Types of constructor

#1. default constructorNote: If you completely omit __init__ from your class, Python automatically provides an empty default constructor behind the 
# scenes so the object can still be createdNote: If you completely omit __init__ from your class, Python automatically provides an empty default constructor behind the scenes so the object can still be createdNote: If you completely omit __init__ from your class, Python automatically provides an empty default constructor behind the scenes so the object can still be createdNote: If you completely omit __init__ from your class, Python automatically provides an empty default constructor behind the scenes so the object can still be createdNote: If you completely omit __init__ from your class, Python automatically provides an empty default constructor behind the scenes so the object can still be created
'''class Car:
    def __init__(self):
        self.wheel=4

my_car=Car()
'''

#2. parameterized constructor
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


# student1=Student('anjan',26)
# student2=Student('om',23)
# print(student1.name,student1.age)

#Writing a function to calculate force
# def calculate_force(m,a):
#     force= m*a
#     return force

# print("force is ",calculate_force(2,3),"newtons")

#main function

'''def main():
    print("hello world")
#Including the main() function allows us to import and run 
# this program in another script.
if __name__=='__main__':
    main()
    '''

# def main():
#     print('This line is printed directly from the main function of the program')
#     secondary_function()

# def secondary_function():
#     print('This line is printed from a secondary function call within the main function')

# if __name__ == '__main__':
#     main()


'''def calculate_minutes(seconds):
    #this function will calculate minutes
    #takind seconds as parameter

    minutes=seconds/60
    return minutes

print(calculate_minutes(60),"minutes")
'''

#this function takes
#one argument num and
#returns its square

'''def square(num):
    numSquare=num*num
    return numSquare

#several cases to verify function is working
print(square(2))
print(square(3))
print(square(4))'''
'''
#INPUT and OUTPUT
# input 
name= input("Enter your name: ")
age= input("Enter your age:")
#OUTPUT
print("nice to meet you ",name,"you are ",age,"years old")
#concatination
print("nice to meet you "+name+" you are "+age+" years old")
#formateed string literal
print(f"nice to meet you {name} you are {age} years old")
print(f"nice to meet you {name.upper()} you are {age} years old")
print(f"nice to meet you {name.capitalize()} you are {age} years old")'''

# name='anjan'
# print('Very nice to meet you, {}!'.format(name))

#VARIABLE IN PYTHON
#declaring variable 
# name='anjan'
# name='Anjan'
# temperature=97.5
# is_raining=True
# sum_of_two_numbers=4+2

#Casting variable
# temperature=str(97.5) #convert to string
#The function str() takes a value and converts it into a string.
#  There are other functions such as int(), float() and bool() .

# int_value= 4
# print(int_value)
# print(type(int_value))
# print()

# float_value=float(int_value)
# print(float_value)
# print(type(float_value))
#GLOBAL VARIABLES
#Outside all functions at the outermost level.
# score=100
# def show_score():
#     print(score)

# show_score()


#LOCAL VARIABLES
#Inside a function, loop, or block.
# def assign_score():
#     local_score=100 #local variable
#     print(local_score) #works perfectly fine inside

# assign_score()


#DATA TYPES
#1. String
'''temp='97.9'
temp=str(97.9)
print(temp)'''
#2. Integer
'''num=100
print(num)
num=int(100.19)
print(num)'''
#3. Float
'''temp= 100.19
print(temp)
temp= float(100)
print(temp)'''
#4. Boolean
'''is_raining=True
print(is_raining)
raining=bool(False)
print(raining)'''

#OPERATORS
#1. Arithmetic operators
'''+,-,*,/,%,**,//,%,'''
'''x=4
y=3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)'''

#2. Relational operators,comparison operators
#result is boolean like True or False
'''
==,!=,>,<,>=,<='''

#3. Logical operators
'''
and,or,not'''
# x=4
# y=3
# x>2 and y>1  #True
# x>5 or y>1 #True
# not (x>2 and y>1) #False



#if elif else
'''score=90
if score>=80:
    print('you passed')'''

'''score=70
if score>=80:
    print('you passed')
else:
    print('you failed')'''

# score=70
# if score>=80:
#     print('you passed')
# elif score>=65:
#     print('you passed but talk to insturctor')
# else:
#     print('you failed')

#LOOPS
#1. for loop   It has two keywords, for and in
'''nums=[1,2,3,4,5]
for num in nums:
    print(num+1) #add 1 to each in element'''

    #for loops witn range()
'''for i in range(5):
    print(i)  #0,1,2,3,,4'''
    #nested for loops
# teams=[['anjan','aakash'],['om','chatra'],['puntey','beer'],['ram','sita']]
# for team in teams:
#     for name in team:
#         print(name)


#2. while loop

'''i=1
while i <=5:
    print(i)
    i+=1'''
#An infinite loop is a while loop that never terminates because the condition is always 
# evaluated to be True. This could be due to a typo or an incorrect logic in the loop. 
# You can terminate the loop by pressing the Ctrl and c together on your keyboard.

#examples of loop 
'''nums=[3,4,16]
print("This is example of for loop")
for num in nums:
    print(num**2)

i = 3
print("Thi is example of while loop")

while i<100:
    print(i)
    i =i**2'''

#PASS BREAK AND CONTINUE

#pass
#The pass keyword is mostly used as a placeholder in a loop. 
# Nothing gets executed when pass is placed under a condition.
'''names=['anjan','om','puntey','ram','sita','manoj','chatra']
for name in names:
    if 'a' in name.lower():#ignore names with 'a' using pass
        pass
    else:
        print(name) '''

#BREAK
'''names= ['anjan','om','puntey','ram','sita','manoj','chatra']
for name in names:
    if 's' in name.lower(): #it breaks program when fount letter o
        break
    else:
        print(name)'''

#CONTINUE
'''names= ['anjan','om','puntey','ram','sita','manoj','chatra']
for name in names:
    if 's' in name.lower(): #s aayo vane ignore natra continue
        continue
    else:
        print(name)''' 

# names = ['Amanda', 'Mercedes', 'Rachel', 'Elisabeth', 'Tay', 'Xavier', 'Joaquin', 'Sam']
# for name in names:
#     if 'm' in name.lower():
#         continue
#     elif 'r' in name.lower():
#         pass    
#     elif 'j' in name.lower():
#         break
#     else:       
#         print(name)

#ERROR HANDLING
#try: 
'''nums= [0,1,2,3,4,5,6]

try:
    print(sum(nums))

except:
    print('cant print sum! your variable are not numbers')
finally:
    print('this will always run') #this execute,in cases where both try and except might fail
# # except:'''

# num=['a','b','c']
# try:
#     print(sum(num))
# except:
#     print('can\'t print sum! your variable are not numbers')
# finally:
#     print('this will always run')

# nums=[5,2,3,10]
# try:
#     avg =sum(nums)/len(nums)
#     print(f'The avg is: {avg}')
# except:
#     print('can\'t print sum! your variable are not numbers')
# finally:
#     print('this will always run')

#FUNCTION BASICS
#creating a function
'''def add_three(n1,n2,n3):
    sum_three= n1+n2+n3
    return sum_three
sum_output=add_three(1,2,3)
print(f'The sum of number is: {sum_output}')

#using a function
sum_output= add_three(1,2,3)
#parameters
1,2,3
#arguments
add_three(1,2,3)
'''
'''def greetings(language):
    if language=='spanish':
        print('Hola')
    elif language=='french':
        print('Bonjour')
    elif language=='english':
        print('Hello')
    print('greeting')
#this is argument actually
greetings('spanish')'''

#RECURSION
#word recursion in Python describes the process 
# of repeatedly calling a function within itself
#IT has base case num==1 ,and recursive ie factorial(num-1)which call func factorial itself again
#if base case not mention it will infinite loop 
'''def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
f=factorial(5)
print(f)'''

'''num =5
factorial=1

for i in range(1,num+1): #range(start,stop,steps) start 1 ,stop 5
    factorial *=i #i = 1,2,3,4,5 and multiply all i save to factorial

print(f'the factorail of {num} is {factorial}')'''

#visualize recursion 
'''def factorial(num):
    call_stack=[]
    if num==1:
        print("Base case reached Num is 1.")
        return 1
    else:
        call_stack.append(num)
        print(call_stack)
        return num*factorial(num-1)
print(factorial(5))'''



'''#LAMBDA FUNCTIONS
#Lambda functions, also known as anonymous functions, are small,
# inline functions that can have any number of arguments but only one expression

def square(num):
    return num**2

square_lambda= lambda x: x**2 #syntax is : lambda[arguments]:[expression]

print(square(2))
print(square_lambda(2))

add_num = lambda a,b: a+b
print(add_num(2,3))

greeting= lambda name:f"Hello {name} !"
print(greeting('anjan'))'''

'''#even check
numbers =[1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x%2==0,numbers)) # create new list and apply filter
square= list(map(lambda x: x**2,numbers)) # map uses on each element oon same list
print(even_numbers)
print(square)'''

#CLASSES AND OBJECTS
#classes
#A class is a data type that encapsulates information and functions as a blueprint for objects
'''class Dog:   #class name
    pass
pepper=Dog()  #instance of class is objects,pepper is object
print(pepper)'''

#CONSTRUCTORS AND DESTrUCTORS
'''in object-oriented programming (OOP), constructors are functions 
that are called when an object of a class is created and destructors are called 
to delete an object. 
In this article, we’ll cover the following:

Constructors
Destructors'''
#Constructors __init__()
''' the __init__() method would be called every time the ClassSchedule 
class is instantiated, and used to initialize a newly created object:'''
'''class ClassSchedule:
    def __init__(self,course): #self parameter in init method refers to current object
        self.course=course  #course allows input to assigning value

        #let create an instance varible Chemistry and assign to obj first

first = ClassSchedule('chemistry')
print(first.course)'''

#Destructors __del__() method
'''class ClassSchedule:
    def __init__(self,course):
        self.course=course
        #Destructors are special functions that are called when an object gets deleted
    def __del__(self):
            print('ClassSchedule object deleted')
first= ClassSchedule('chemistry')
print(first.course)
del first'''



#Encapsulation

#Used ACcess modifier Public ,private _prefix, protexted __prefix
#solve using google

# class UserInfo:
#     def __init__(self,username,email_address):
#         self.username=username
#         self.email_address = email_address

# user = UserInfo('anjan123','njan@gmail.com')
# print(user.username)
# print(user.email_address)
#Class method

'''class UserInfo:
    def __init__(self,username,email_address):
        self.username=username
        self.email_address = email_address
    def check_username(self,username_to_check):
        if username_to_check ==self.username:
            return True
        else:
            return False
user = UserInfo('anjan123','njan@gmail.com')
print(user.check_username('anjan123')) #True
print(user.check_username('anjan')) #false'''


#Inheritance
# that enables the transfer of methods and properties of one class to another.
#  Inheritance allows for reusability of code as well as extending the capability of new classes
#Parent class and child class
#PARENT CLASS also known as base class whose method are inherited by child class
#simple class too understand
'''class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def show_name(self):
        print(f"{self.name} is {self.age} years old")

data= Person('anjan',26)
data.show_name()
#child class
'''
#Base or parent class
'''class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def show_info(self):
        print(self.name)
        print(self.age)
#child classs
class Teacher(Person):
    def __init__(self,name,age,subject):
        self.subject = subject

        Person.__init__(self,name,age)  #inheriting from person class

teacher = Teacher('anjan',26,'physics')
teacher.show_info()
print(teacher.subject)'''

'''
Polymorphism with Classes
In Python, classes are allowed to contain methods that share the same name as another 
method from a different class. The code below shows two different classes that are
 independent of each other with some methods of the same names:

class Checking():
   def type(self):
       print('You have a checking account at the Codecademy Bank.')
 
   def balance(self):
       print('$20 left in your checking.')
 
class Savings():
   def type(self):
       print('You have a savings account at the Codecademy Bank.')
  
   def balance(self):
       print('$1000 left in your savings.')

We can create an object for each class, and without worrying
 about which object belongs to which class, we can call the same methods. 

account_a = Checking()
account_b = Savings()
 
for account in (account_a, account_b):
   account.type()
   account.balance()

'''

#DATA STRUCTURE 
#LIST,[1,2,3],mutable,ordered,allows duplicate values,
#tuple,(1,2,3),immutable,ordered,allows duplicate values,
#set,{1,2,3},mutable,unordered,not allows duplicate values,
#dictionary,{key:value},mutable,unordered,allows duplicate values
#LIST
'''lst = ['abc', 123,'def', 10.5, 62, ['g','h','i']] #6 items 0-5
#indexing and slicing
print(lst[0])
print(lst[4:6]) # slice /4-5 is / 6th is ignored
print(lst[-1])'''

#BUILD IN method
'''lst = ['abc', 123,'def', 10.5, 62, ['g','h','i']] 
print(len(lst))

lst = ['abc', 123,'def', 10.5, 62, ['g','h','i']] 
lst.append(99) #append put item on last of list
print(lst)

lst = ['abc', 123,'def', 10.5, 62, ['g','h','i']] 
lst.remove(62,) #remove items
lst.remove('abc')
print(lst)

lst = ['abc', 123,'def', 10.5, 62, ['g','h','i']] 
lst.pop() #remove last item
print(lst)
lst.pop(0)
print(lst)'''


#tuple,(1,2,3),immutable,ordered,allows duplicate values,
#indexing and slicing are same
#method are :len(),max(),min(),.index(),.count()


#DICTIONaries
#dictionary,{key:value},mutable,unordered,allows duplicate values
'''#eg of dictionary
groceries ={
    'fruits':['mangoes','banana','kiwis'],
    'vegetables':['tomatoes','carrots','onions'],
    'drinks':['water','juice','tea']

}'''
#accesing and writing values
#In contrast to other data structures such as lists and tuples, there are no built-in ways
#  to use indexing and slicing to access the values in a certain order
#  in the dictionaries. A value within a dictionary can be accessed with its key.
party_planning={
    'yes':10,
    'no':15,
    'maybe':30,
    'location': 'garden',
    'date':'2026/07/10',
}
'''print(party_planning['location']) #return garden
#updating values
party_planning['location']='riverside'
print(party_planning) #prints riverside
#adding new items
party_planning['music']='rock'
print(party_planning)'''

#built in functions
#len()
# print(len(party_planning))

'''#.update()
shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}
 
shopping_list1.update(shopping_list2)
 
print(shopping_list1)

#.keys() and . values()
print(shopping_list1.keys())
print(shopping_list1.values())'''


#DSA 
#Queues
#FIFO
'''
from node import Node
class Queue:
    #initializing the queue
    def __init__(self):
        self.head= None #head of the queue is none meaning empty [0 index]
        self.tail = None  #tail of the queue is none meaning empty [-1 index]
        self.size = 0  #size of the queue is 0 meaning nothing inside

    #method or operatons enque,dequeue,peek,size,empty
    def enqueue(self,value):
        item_to_add= Node(value)
        print("Adding: "+ str(item_to_add.get_value() +' To the queue!'))
        if self.is_empty():
            self.head = item_to_add
            self.tail = item_to_add
            self.size = 1
        else:
            self.tail.set_next_node(item_to_add)
            self.tail = item_to_add
            self.size += 1    
    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print(str(item_to_remove.get_value()) + " is served!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
                self.size -= 1
                return item_to_remove.get_value()
        else:
                print("The queue is totally empty!")


    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")
     
    def get_size(self):
        return self.size
  
    def is_empty(self):
        return self.size == 0
 


print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue()
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
#deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\n Our first order will be " + deli_line.peek())
print("------------\n Now serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()'''

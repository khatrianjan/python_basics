###########   LIST    #######################
#1) create a list of 5 integer entered by user. print the sum of all elements
""" hint use a loop to take 5 input and sum() function"""

# digit =[]
# for i in range(5):
#     num = int(input("enter the number: "))
#     digit.append(num)
# print(digit)
# print("The sum of all digit is : ",sum(digit))

###############################################################
# 2)write a program to count how many times a number appears in a list
"""use list.count(x) method"""
#numbers= []
# # if numbers == int("q"):
# digit=5
    

# for i in range(5):
#     num = int (input("Enter a number: "))
#     numbers.append(num)
# x= numbers.count(digit)
# print(f"The number"x)

#############################################
# 3) write a program that removes all even numbers from a list
"""use a loop with if number % 2 != 0."""
# even = [1,2,3,4,5,6,7,8,9,]
# for ev in even:
#     if ev %2 ==0:
#         even.remove(ev)
# print(even)
############################################

# 4) FIND THE LArGEST AND SMALLEST ELEMENT IN A LIST 
"""USE max() AND min() FUNCTIONs"""
# Elements=[]
# for i in range(5):
#     num = int(input("Type a number: "))
#     x = Elements.append(num)
# print(f"The List of number is: {Elements}")
# print(f"The maximum no. is: {max(Elements)}")
# print(f"The minimum  no. is: {min(Elements)}")
###################################################################

# 5) sort a list of number in ascendind order.
"""use list.sort() or sorted(list)"""

# Elements=[]
# for i in range(5):
#     num = int(input("Type a number: "))
#     x = Elements.append(num)
# print(Elements)
# print(f"The ascending order of the list is: {sorted(Elements)}" )
###############################################################################

# 6)create a list of fruits .ask  user to enter fruits and check if its in the lis
"""use in keywords to check membership"""
# print("create a list of fruits. ")
# fruits=[str]
# for i in range(4):
#     for check in fruits:
#         ad = str(input("Enter the fruits name: "))
#         fruits.append(ad)
#         break
# print("Type fruit name,U wanna check if it is in List or not.")
# x = str(input(""))
# if x in fruits:
#     print({x} ,"is in the list")
#     print("u r awesome in guessing.")

#####################################################################
# 7) reverse the elements of a list without using reverse() function
"""use slicing list[::-1] or looop to reverse manually"""

# Elements=[]
# reverse_list = []
# for i in range(5):
#     num = int(input("Type a number: "))
#     x = Elements.append(num)
# print (Elements)

"""slicing technique to reverse"""

# reverse_list = Elements[::-1]
# print(reverse_list)

"""to reverse item manually using loop"""

# for item  in Elements:             
#     reverse_list. insert(0, item)
# print(reverse_list)

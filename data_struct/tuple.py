"""TUPLE"""
########################################
# 1)create a tuple with 5 elements and display its length
"""hint use len() function """
# elements = ('a','b','c','d','e')
# print(len(elements))

#################################################

#2) Ask the user to enter 5 number and store them in a tuple. Then display their average
"""hint convert input to int, use sum and len()."""

# num= []
# for i in range(5):
#     a = int(input("Enter the num: "))
#     num.append(a)
# print(num)
# converted_num = tuple(num)
# print(converted_num)

# avg = sum(converted_num)/len(converted_num)
# print(f"The Avg of the number is: {avg}")

########################################################
# 3) check if a specific number into a tuple
"""use in keyword"""

# number=(10,20,30,40,50,60)
# check= int(input("Enter the number to check in the tuples: "))

# if check in number:
#     print(f"{check} is in the tuples.")
# else:
#     print(f"{check } is not in the tuples")

#################################################################
# 4)convert  a list of num into tuples
# lis=[1,2,3,4,5]
# print(tuple(lis))
##############################################

# 5)write a program to find the index of a number in tuple
"""use tuple.index(x)"""
# a_tuple = (1,2,3,4,5,6,7,8,9)
# print(a_tuple.index(5))
########################################################
"""this will raise an errror --- explain immutabily"""
##################################################
####Focus FOR<=,WHile< and nested loop##########

###########SIMPLE##########################
#1)print NUmber from 1 to 10
"""input N and print all numbeer use range(1,N+1)"""

# n = int(input("enter any number: "))
# for i in range(1,n+1):
#     print(i)
############################
#2)sum of First N natural number
"""input n and print the sum
use  loop to add each num to total variable"""

# n = int(input("enter the number: "))
# total_val = 0
# for i in range(1,n+1):
#     print(i)
#     total_val+=i
# print("the total sum is:",total_val )

#################################################
#3)print multiple of 3 upto N
"""input N and print all mupliple of 3 upto N
use if i%3 ==0 inside loop"""
# n = int(input("enter upto where u wanna multiply"))
# for i in range(1,n+1):
#     if i %3 ==0:
#         print(i)
######################################################
#4)count Digit in a number
"""use while number >0 and divide by 10 each time
input a number and count how many digit it has"""

# num = int(input("Enter a number: "))

# # Make number positive
# num = abs(num)

# Special case for 0
# if num == 0:
#     digit_count = 1
# else:
#     digit_count = 0
#     while num > 0:
#         digit_count += 1
#         num //=10

# print("Number of digits:", digit_count)

#####################################################
num = 23435
# count = 0
for i in range(num):
    if i ==0:
        i= num%10
    
print(i)

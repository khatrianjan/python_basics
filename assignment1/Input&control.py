#1 even or odd
"""ask user for number. use the mudulo operator to check if it is
divisible by 2"""

#number = int(input("enter any number:"))   #int is necessary
#if number % 2 ==0:
#    print("it is even")
#else:
#    print("it is odd") 

###########################################################################

#2 positive negative or 0
"""use if elif ans else """


#number = int(input("enter any number:"))
#if number >0:
#    print("it is positive.")
#elif number<0:
#    print("it is negative.")
#else:
#    print("it is 0.")

###############################################
#3 largest of two number
"""ask user two input and find the larger one"""

#num1 =int(input("Enter first number: "))
#num2 = int(input("Enter second number:"))   
#if num1 > num2:
#    print(num1 ," is the greater.")
#elif num2 > num1:
#    print(num2, " is the greater.")
#else:
#    print("It is equal.")

##################################################
#5) Divisible by 5 and 11
"""use if number %5 and number %11 ==0"""

#num = int(input("Enter the number: "))
#if num %5==0 and num% 11 ==0:
#    print(f"The {num} is divisible by 5 & 11.")
#else:
#    print(num,"is not divisible")
#####################################################

#6) Leap year checker
"""input a year , It is a Leap if
Divisible by 4 and not by 100
or Divisible by 400"""

"""year = int(input("Enter year: "))
if (year %4 ==0 and year % 100 != 0) or (year % 400==0):
    print(f"The {year} is  leap year.")
else:
    print("it  is not leap year")"""

############################################################
#character type checker
"""use .isalpha(),.isdigit(),or ascii with ord()"""

"""string =input("Enter char:")
if string.isalpha()== True:
    print("IT is alphabet")
    print(f"{string} ascii is:", ord(string))
if string.isdigit()==True:
    print ("it is digit")"""
###################################################
 #8) UPPERCASE or lowercase alphabet

"""string = input("Enter any alphabet:")
if string.isupper():
    print(f"it is uppercase./t {string} value is ",ord(string))
else:
    print(f"{string} value is:" ,ord(string))"""

########################################################

#9) weekday Name by Name
"""input a number (1-7) and the the weekday using chain of if elif else"""
"""day = int(input("enter a number:"))
if day ==1:
    print("It is sunday ")
elif day ==2:
    print("It is  monday") 
elif day ==3:
   print("It is  tuesday")
elif day ==4:
    print("It is  wednesday")
elif day ==5:
    print("It is  Thrusday")
elif day ==6:
    print("It is  friday")
elif day == 7:
    print("it is saturday.")"""

############################################
#10) grade assigner
"""marks =  int(input("Enter Your Marks: "))
if 90<=marks<= 100:
    print("A+")
if 80<=marks<= 90:
    print("A")
if 70<=marks<= 80:
    print("B+")
if 60<=marks<= 70:
    print("B")
if 50<=marks<= 60:
    print("C+")
if 30<=marks<= 50:
    print("C")
if 30<=marks<= 32:
    print("fail")"""

#######################################
"""MODERATE QUESTION"""
######################################
#12)Quadrant Finder
"Input X and Y and print in which quadraant lies"
"""x,y = map((input("X,Y: "))).split()

if x>0 and y>0:
    print("Lies in 1st Quadrant")
if x<0 and y>0:
    print("Lies in 2nd Quadrant")
if x<0 and y<0:
    print("Lies in 3rd Quadrant")
if x>0 and y<0:
    print("Lies in 4th Quadrant")"""
###############################################

#14) odd or even digit count
"""phase =input("Enter phase: single / 3 phase ")
unit = int(input("Enter the bill units: "))



if phase =="single":
    if unit <= 20:
        print(unit *4 )
    elif 21<= unit<= 30:
        print(unit*7)

if phase == "3 phase":
    if unit<=400:
        print(" your payment is : rs4400")
    else:
        print(12* unit)"""
###################################################################

#15)simple calculator
#take two number and operator from user and perform calculation
"""a= int(input("Enter the number:"))
b = int(input("enter another number: ")) 
op = input((" select one of these:  +  , -  ,*  ,   /\n"))

if op =='+':
    print(f"The sum of {a} and {b} is : ", {a+b})
if op =='-':
    print(f"The difference of {a} and {b} is: " ,{a-b})
if op =='*':
    print(a*b)
if op =='/':
    print(a/b)"""
#########################################################
#16) Absolute value calculator

"""num = int(input("Enter the num: "))
if num >0:
    print(num)
if num <0:
    print(f"It is non integer so \n Its Absolute value is: ", {num * -1})"""
#######################################################################################
#17) check if character is vowel or constant
"""vowel =("a","e","i","o","u")
character= str(input("Enter any character in keyboard: "))

if character in vowel:
    print("it is vowel.")
else:
    print("it is consonant")"""
###################################
#18 check traingle type
"""Input three side check if all equal equilateral, 2 side = isoscelec all 
diff== scalene"""
"""
a = int(input("enter a side of triangle in cm: "))
b = int(input("enter b side of triangle in cm: "))
c = int(input("enter c side of triangle in cm: "))
if a==b and b==c:
    print("equilateral traingle")
if a==b or b==c or a==c:
    print("It is isosceles triangle")
else:
    print("it is scalene")"""
#####################################################
#20)password strength checker
"""word= str(input("enter a password:"))

if len(word)<=8:
    print("false")
    print("retype password")

word= str(input("Enter any password"))
has_digit= False
has_letter=False

for char in word:
    if char.isdigit():
        has_digit=True
    elif char.isalpha():
        has_letter=True

if len(word)>=8 and has_digit and has_letter:
    print("password is valid")"""
        



    





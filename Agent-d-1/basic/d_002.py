# 3. Logical Operators:
'''
a = 10
print("AND Operator Results:")
print(a>10 and a<20)
print(a==10 and a<20)
print(a==10 and a>20)
print(a<10 and a>20)


print("OR Operator Results:")
print(a>10 or a<20)
print(a==10 or a<20)
print(a==10 or a>20)
print(a<10 or a>20)

print("NOT Operator Results:")
print(not(a>10)) 
'''
# Input Validation

# unsafe: 

#age = int(input("Enter your age:"))
# if user type alphabate so program will crash with ValueError

''' 
# Take two numbers and print their sum, difference, product, and quotient.
# safe way to hanlde the user input:
try:
    age = int(input("Enter your age:"))
    if age > 0:
      print("Your age is:", age)
    else:
       print("Age cannot be negative or zero!")
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")

    '''

'''
# Addition of two numbers with input validation
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(f"you enter the number is {num1} and {num2}")
    sum = num1 + num2 
    print(f"Sum is : {sum}")
except ValueError:
    print("Invalid input! Please enter valid integers for both numbers.")


# Subtraction of two numbers with input validation
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(f"you enter the number is {num1} and {num2}")
    sub = num1 - num2 
    print(f"Subtraction is : {sub}")
except ValueError:
    print("Invalid input! Please enter valid integers for both numbers.")


# Multiplication of two numbers with input validation
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(f"you enter the number is {num1} and {num2}")
    multiplication = num1 * num2 
    print(f"Multiplication is : {multiplication}")
except ValueError:
    print("Invalid input! Please enter valid integers for both numbers.")

# Devision/quotient of two numbers with input validation
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(f"you enter the number is {num1} and {num2}")
    devision = num1 / num2 
    print(f"Devision is : {devision}")
except ValueError:
    print("Invalid input! Please enter valid integers for both numbers.")
'''
'''
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(f"you enter the number is {num1} and {num2}")
    reminder = num1 % num2 
    cube = num1 ** 3
    square = num1 ** 2
    print(f"Reminder is : {reminder}")
    print(f"Square is : {square}")
    print(f"Cube is : {cube}")
    
except ValueError:
    print("Invalid input! Please enter valid integers for both numbers.")

'''

'''
try:
    num1 = int(input("Enter a number:"))
    if num1%2==0:
        print("Even Number")
    else:
        print("Odd Number.")

except ValueError:
    print("Invalid input! Please Enter Valid Integers for both numbers.")

'''
'''
try:
    minutes_1 = int(input("Enter Minutes:"))
    get_hours = minutes_1//60
    get_minutes = minutes_1%60

    print(f"So you enter the minutes is {minutes_1}, and this is convert into hours and minutes, so now you can read it like {get_hours} hours and {get_minutes} minutes. ")
except ValueError:
    print("Invalid input! Please Enter Valid Integers for both numbers.") 


'''


# Intermediate Level
# Ask the user for 3 numbers and print the largest.
'''
try: 
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    if num1>num2 and num1>num2:
        print(f"{num1} is largest number.")
    elif num2>num1 and num2>num3:
        print(f"{num2} is largest number.")
    else:
        print(f"{num3} is largest number.")

except ValueError: 
    print("Invalid input! Please enter valid integers. ")
'''

#Write a program to check if a number is divisible by both 3 and 5.
'''
try: 
    num1 = int(input("Enter number:"))
    if num1%3==0 and num1%5==0:
        print(f"{num1} is divisible by 3 and 5")
    elif num1%3==0 and num1%5!=0:
        print(f"{num1} is divisible by 3, but not divisible by 5.")
    elif num1%3 != 0 and num1%5==0:
        print(f"{num1} is divisible by 5, but not divisible by 3.")
    else: 
        print(f"{num1} is not divisible by both 3 and 5.)

except ValueError:
    print("Invalid number! Enter  Valid Integer number.")

'''

#Take two inputs — check if both are positive using logical and.

'''
try: 
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number."))

    if num1>=0 and num2>=0:
        print(f"{num1} and {num2} both are positive")
    elif num1>=0 and num2<0:
        print(f"{num1} is positive number and {num2} is negative number.")
    elif num1<0 and num2>=0:
        print(f"{num1} is negative number and {num2} is positive number.") 
    else:
        print(f"{num1} and {num2} both are negative.")

except ValueError:
    print("Invalid input, Please enter the integernumber. ")

'''

# Ask the user for their marks — print whether they passed (>=40) or failed.
'''

try: 
    marks = int(input("Enter your marks: "))
    if marks >= 40: 
        print("Congratulation! You are Passed.")
    else:
        print("Sorry! You are failed.")

except ValueError:
    print("Invalid marks! Please enter the valid marks in the integer form.")

'''

# Ask for an age and check if it’s between 18 and 60 (inclusive).
'''
try: 
    age = int(input("Enter your age: "))
    if age>18 and age<60:
        print(f"{age} Age is the inclusive")
    else:
        print(f"{age} is a exclusive.")
except ValueError: 
    print("Please Enter the Valid Age number in the integer form.")

'''

'''
import math

try:
    num1  = int(input("Enter first number:"))
    num2 = int(input("Enter second number: "))
    operation = input("Enter a valid operation (+, -, *, /, %, **, square root):")

    if operation == '+':
        result = num1 + num2
    
    elif operation =='-':
       result = num1 - num2 
    
    elif operation == '*':
       result = num1 * num2
    
    elif operation == '/':
       if num2==0:
          print("Please enter the valid integer because Zeri divison not allowed.")
       else:
         result= num1/num2

    elif operation == '%':
       result =  num1%num2
    
    elif operation == '**':
       result = num1 ** num2

    elif operation == 'square root':
       result = math.sqrt(num1) , math.sqrt(num2)
    
    else:
        print("Invalid operator!")
        result = None
    result = round(result,2)
    if result is not None:
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    
except ValueError:
    print("Invalid Number, Enter the valid integer number.")
'''

# result = 10 + 3 * 2 ** 2 - 8 // 3
# print(result)



# print() is how we show data to the user.
'''
print("Hello, world.")
print("I am",22, "years Old.")
name = "subhash"
age = 22
print(f"Hello, my name is {name} and I am {age} years old.")


# User Input: 
# use input to get the user data:

name = input("Enter your name: ")
age = int(input("Enter your age:"))
print(f"Hello, your name is {name} and your are {age} years old. and next year you will be {age+1}: years old.")


'''

# Baisc Exercise: 
# 1 Print your name, age, and favorite color.
# name = input("Enter your name:")
# age = int(input("Enter your age: "))
# color = input("Enter ypour favorite color: ")
# print(f"Hello,, my name is {name} and i am {age} years old and my favorite color is {color}.")

# # 2 : Add two numbers and print the result.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# sum = num1 + num2 
# sub = num1 - num2 
# multiplication = num1*num2
# devision = num1/num2
# modulas = num1 % num2 
# flor = num1 // num2 
# sqr = num1 ** 2, num2 ** 2
# cube = num1 ** 3, num2 ** 3


# print(f"the sum of {num1} and {num2} is {sum}.")
# print(f"the subtraction  of {num1} and {num2} is {sub}.")
# print(f"the multiplication of {num1} and {num2} is {multiplication}.")
# print(f"the devision of {num1} and {num2} is {devision}.")
# print(f"the modulas of {num1} and {num2} is {modulas}.")
# print(f"the flor devision of {num1} and {num2} is {flor}.")
# print(f"the square of {num1} and {num2} is {sqr}.")
# print(f"the cube of {num1} and {num2} is {cube}.")



# 3. Convert temperature from Celsius to Fahrenheit.

# temperature = float(input("Enter temperature in celcius: "))
# fahrenheit = (temperature * 9/5)+32
# print(f"{temperature} degree celcius is equal to the {fahrenheit} degree fahrenheit.")


# 4 : Take your name from input and print a greeting.

# name = input("Enter your name: ")

# print(f"Hello,{name}! Good to see you.")


''' 
# 4:  Swap two varialbe values without using the third varialbe.

a = int(input("Enter the firsat varialbe value : "))
b = int(input("Enter the second varialbe value : "))

print(f"Before swappiing the varialbe: a = {a}, b = {b}")

# after swapping the varialbe without using the third varialbe.
a,b = b,a 

print(f"After swapping the varialbe a = {a}, b = {b}")

'''


'''
# swappingt the vairalbe value by using the third varialbe.

a = int(input("Enter the first varialbe number: "))
b = int(input("Enter the second varialbe number: "))
print(f"Before swapping the varialbe a = {a}, b= {b}")

temp = 0
temp = a
a = b
b = temp

print(F"After swapping the varialbe by uisng the third varialbe a = {a}, b = {b}")


'''

#  Intermediate Level: 

'''
# 1 Calculate the area of circle given the radius.
import math

radius = float(input("Enter the radius of circle: "))

# area = 3.14159*(radius**2)
areas = math.pi *(radius **2)

print(f"The area of circle with radius {radius} is {areas}.")

'''

# 2 write the script to ask the question and store the answer.
'''
name = input("WHat is your name?")
age = int(input("How old are you?"))
city = input("What city do you live in?")

print(f"Hello,{name}!, Your are {age} years old and you live in {city}.")
'''

# Mini Project — “About Me” Program
'''
🧩 Problem:

Create a program that:
Takes your personal info as input
Does one simple math operation
Prints a neat summary  

'''
# take the user personal information: 
name = input("WHat is your name? ")
age = int(input("How old are you?"))
city = input("What city do you live in?")
color = input("WHat is your favorite color?")
dob_date = int(input("Enter your birth date: "))
dob_month = int(input("Enter your birth month: "))
dob_year = int(input("Enter your birth year: "))
hobby1 = input("Enter your first hobby: ")
hobby2  = input("Enter your second hobby:")

# simple math operation :
next_year_age = age + 1

# Here we calculate the exact age based on the current year.:
current_year = 2025
current_month = 10
current_date = 24

user_years = current_year - dob_year
user_months = current_month - dob_month
user_days = current_date - dob_date






# print the summary: 
print(f'''
Here are the full summary of your life: \n 
Hello, {name}!, Wleocme to My Universe. \n 
You are {age} years old, and next year you will be {next_year_age} years old. \n 
You live in {city}. \n and your favorite color is {color}. \n 
Your exact age is {user_years} years, {user_months} and {user_days} days old.\n 
Your hobbies are:\n  1.{hobby1}\n 2.{hobby2}.\n
\n Have a great day!
''')


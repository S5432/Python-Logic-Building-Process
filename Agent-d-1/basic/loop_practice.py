
''' 

for i in range(5):
    print("Hello", i)

    '''

'''
for i in range(2,11,2):
    print(i)

    '''
'''
# white loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
'''


# Concept 3: break and continue

# break: exits the loop early.

# continue: skips to the next iteration.

'''
for i in range(1,6):
    if i == 5:
        break
    print(i)
'''
'''
for i in range(1,6):
    if i==4:
        continue
    print(i)

    ''' 

# Concept 4: Loop + else
# The else block runs only if the loop completes normally (no break).
'''

for i in range(1,6):
    print(i)
else:
    print("Loop completed successfully.")

'''
'''
for i in range(1,6):
    if i == 4: 
        break
    print(i)
else:
    print("Loop not complete succesfully.")

'''


# 💪 Day 4 Practice Exercises
# 🧩 Easy Leve:

'''
# Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i,"number.")

    '''

'''
# Print even numbers from 2 to 20 using a while loop.
number  = 2
while number <=20 :
    if number%2==0:
        print(number)
    number += 2


    '''
'''
# Calculate the sum of first 10 natural numbers using a for loop.
number = 1
sum = 0

while number <=10:
    print("Sum of natual number:", sum)
    number += 1
    sum = sum+number

    '''

'''
# Use break to stop the loop when number = 7.
number = 1

while number <=10:
    if number == 7:
        break
    print(number)
    number += 1

'''

'''
# Use continue to skip printing number 5.
number = 1

while number <= 10:
    if number == 5:
        continue
    print("number:", number)
    number += 1
'''
'''
#Ask user for 5 numbers and print their total sum.
number = 0
count = len(str(abs(number)))
sum = 0

while count <=5:
    number = int(input("Enter number:"))
    print("count: ", count)
    count += 1
    sum = sum + number
print("Total Sum is: ", sum)

'''
'''
# Ask user for a word and print each letter separately.
word = input("Enter a word:")

count = len(str(word))
num = 0
while num <=count:
    print(word[num])
    num += 1

'''

'''
# Create a countdown timer (10 → 1).
countdown = 10

while countdown>=1:
    print("Countdown:", countdown)
    countdown = countdown-1

    '''
'''
# Check if a number is prime using a loop.

num = int(input("Enter a Number : "))

if num%1==0 and num%num==0:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

    '''

# pirnt the Hello 5 times

# for i in range(5):
#     print("Hello!")




# for i in range(5):
#     print(i)


# count = 1

# while count <=5:
#     print(count)
#     count += 1



# for i in range(5):
#     print(i)


# for i in range(1,6):
#     print(i)


# for i in range(1,10,2):
#     print(i)


# for i in range(2,11,3):
#     print(i)



# fruits = ["apple", "banana","cherry"]

# for fruit in fruits:
#     print("I Like", fruit)


# for i in range(10):
#     if i == 6:
#         break
#     print(i)


# for i in range(1,15):
#     if i==6:
#         continue
#     print(i)

# ercise 1: Print 1 to 10
# for i in range(1,11):
#     print(i)

# Exercise 2: Print only even numbers from 1 to 10

# for i in range(11):
#     if i%2==0:
#         print(i)


# Exercise 3: Print multiplication table of 5

# for i in range(1,11):
#     print(f"5 x {i} = {5*i}")

# Exercise 5: Ask user to enter numbers until they type "done", then print sum

# total =0

# while True:
#     num  = input("Enter a number or done..")
#     if num == "done":
#         break
#     total += int(num)
# print("Sum:", total)


# Example: # Print all numbers from 1 to 20 except multiples of 3

# for i in range(1,20):
#     if i%3==0:
#         continue
#     print(i)


#----------------------------------Loop Exercise ---------------------------------#

# Print numbers from 1 to 10 (inclusive) using a for loop.

'''
PBS method

for i in range(1,10)

but inclusive 10

for i in range(1,11)

'''

# for i in range(1,11):
#     print(i)

# Exercise 2: Print Even Numbers (1 to 20)

'''
# PBS method

for i in range(1,21):
    print(i)

# but print only even number

for i in range(1,21):
    if i%2==0:
       print(i)




'''

# Exercise 2: Print Even Numbers (1 to 20)

# for i in range(1,21):
#     if i%2==0:
#         print(i)




# Exercise 3: Sum of First N Numbers

'''
PBS method:
natural numbers  = 1,2,3,4,5,6...
sum  = 1+2  = 3

num = int(input("Enter a number:))
i = 0
sum =0
while i<=num:
   print(num)
   sum = num
   i += 1
print("Sum:", sum)
    
    

'''

# i = 0 
# sum = 0
# num = int(input("Enter a Natural Number: "))

# while i<=num:
#     #print(num)
#     sum = sum+i
#     i = i+1
# print("Sum:", sum)



# Exercise 4: Reverse Countdown: Print numbers from 10 down to 1, then print "Go!"

'''

while i>=1:
  print(i)
print("Go!")
   

'''

# num = int(input("Enter a number:"))

# while num>=1:
#     print(num)
#     num = num-1
# print("Go!!")


# Exercise 5: Multiplication Table for 7

'''
for i in range(1,11):
   print(f"7 x {i} = {7*i}")

'''

# num  = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")


# Exercise 6: Skip Multiples of 3:
'''
# Print numbers 1 to 15, but skip any multiple of 3.

for i in range(1,15):
     if i%3 ==0:
        continue
     print(i)
'''

# for i in range(1,15):
#     if i%3==0:
#         continue
#     print(i)


# Exercise 7: Find First Multiple of 7

'''
we have to use while loop because we do not know the range.

while True:
   num = int(input("Enter a number:))
   if  num%7 == 0:
       print(num)
       break
    


'''

# while True:
#     num = int(input("Enter a number:"))
#     if num % 7 == 0:
#         print(num)
#         break


# Exercise 8: Count Vowels in a Word: 
'''
Ask user for a word.
Count and print how many vowels (a,e,i,o,u) it has.
Use for loop + if.
'''


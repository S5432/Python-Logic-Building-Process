
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

# Find factorial of a number (e.g., 5! = 120).

num = int(input("Enter the number: "))

factorial = 
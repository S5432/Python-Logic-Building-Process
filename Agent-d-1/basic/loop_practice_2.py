# prime number

# num = int(input("Enter a number."))
# is_prime = True

# if num >1:
#     for i in range (2, num):
#      if num%i==0:
#         is_prime = False
#         break
# else:
#    is_prime= False

# if is_prime:
#    print(f"{num} is prime number")
# else:
#    print(f"{num} is not a prime number.")


# -------------- Sum of Natural Numbers (Simplified) --------------#

# sum_num = 0

# for i in range (1, 11):
#     sum_num += i
# print(f"SUm of the first 10 natural number is {sum_num}")


#----------“Skip Printing 5” – Infinite Loop Fix----------


# number = 1
# while number <=10:
#    if number==5:
#       number += 1
#       continue
#    print("number", number)
#    number += 1


#-----------------------------
# number = [1,2,3,4,5,6]

# for i in number:
#     print(i)


#-----------------------------
# counter = 0

# while counter<5:
#     print(counter)
#     counter += 1


#------------- Factorial
# result = 1
# n = int(input("Enter a number:"))
# for i in range(1,n+1):
#     result *= i
# print(f"Factorial of {n} is {result}")



#------------

# result = 1
# counter = 1
# n = int(input("Enter a number:"))

# while counter<=n:
#     result *= counter
#     counter += 1

# print(f"Factorail of the {n} is {result}")


#------------
# numbers = [1,2,3,4,4,3,2,1]
# print("Iterating ove the list using a for loop.")

# for i in numbers:
#     print(i, numbers[i])

#-----------------------
# range() function

# print("Printing the numbers form the 0 and 4 uisng the range().")
# for num in range(1,10,2):
#     print(num)

#------------------
# even numbers

# print("Print the even number by using the range() function")
# for i in range(2,11,2):
#     print(i)


# print("Print the Odd number by using the range() function")
# for i in range(1,11,2):
#     print(i)

#-------------------------
# how to avoiding the infinite loop
# counter = 0
# while counter<5:
#     print("This is iteration", counter+1)
#     counter += 1



# #-------------------
# # break statement in the loop
# numbers1 = [1,2,3,4,5,6,7,8,9,10]

# for i in numbers1:
#     print(i)
#     if i==5:
#         print("Breaking  the loop.")
#         break



# numbers2 = [1,2,3,4,5,6,7,8,9,10]

# for i in numbers2:
#     if i==6:
#         print("Skip the 6 number iteration.")
#         continue
#     print(i)


#------------------ Else Clause in th for loop or while loop in python.

# Using the for loop 
#numbers3 = [1,2,3,4,5,6,7,8,9,10,11]
'''
In this functionality i am iterating the all the element 
and also using the else clause for print the msge after completing the 
for loop succesfully.
'''
# for i in numbers3:
#     print(i)

# else:
#     print("For loop iterating the numbers list items succesfully.")
    


'''
In this while loop we iteraitng the counter and then print the succesfully msg.
'''

# counter = 0

# while counter < 11:
#     print(counter)
#     counter += 1

# else:
#     print("We print this loop after succesfully iterating the counter.")


# 9.How do you iterate over both the index and element in a sequence using the enumerate() function?
# fruits = ["apple", "banana","orange", "mango"]

# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, element : {fruit}")


# 10.Explain the concept of a nested loop in Python.

# for i in range(1,6):
#     for j in range(1,11):
#             result = i*j
#             print(f"{i} * {j} = {result}")

# 11.Discuss the use of the pass statement in a loop block in Python.
# for i in range(5):
#     pass

# counter = 0

# while counter<3:
#     pass
#     counter += 1


# 12.How can you use the zip() function in a for loop to iterate over multiple sequences?

# names = ["ram","shyam","mohan","jay"]
# age = [20, 34,12]

# for names, age in zip(names, age):
#     print(f"{names} is {age} years old.")

# 14. What is the purpose of the iter() and next() functions in Python loops?
# numbers = [1,2,3,4,5,6,7,8,9,10]

# iterator = iter(numbers)

# # Retirve the element one by one next() function
# print(next(iterator)) # Output: 1
# print(next(iterator)) # Output: 2

# # use the iterator in a loop
# for num in iterator:
#     print(num)


#15.How do you create an infinite loop using the while statement?

# count = 0 

# while True:
#     print("Iteration:", count)
#     count += 1

#     # add a break condition
#     if count >=5:
#         break


# 16 Discuss the concept of loop control statements (break, continue, and pass) in Python.

# Example 1 : Using the break, continue, and pass in a loop

# for i in range(5):
#     if i==3:
#         print("Breaking the loop at I =", i)
#         break
#     print("Inside the loop at I = ", i)

###-----------------------
# for j in range(5):
#     if j==3:
#         print("Skipping iteration at j = ", j)
#         continue
#     print("Inside the loop at j", j)


# pass example 

# for k in range(3):
#     if k==1:
#         print("Doing nothing at k = ",k)
#         pass 
#     else:
#         print("Inside the loop at k =", k)

# How can you use the else clause with a while loop?

# counter = 0

# while counter <5:
#     print("Inside the loop, counter=",counter)
#     counter += 1

# else:
#     print("Inside the else clause when loop condition is false.")


# Explain the use of the reverse parameter in the range() function for for loops.
# # Normal Loop:
# print("Normal Loop:")
# for i in range(5):
#     print(i, end=" ")

# print("\n")

# Reverse Loop:
# print("Reverse Loop:")
# for i in range(5,0,-1):
#     print(i, end= " ")


# How do you use the sorted() function in conjunction with a for loop?

# # Original list 
# numbers = [4,3,5,6,2,3,1]

# # Sorted list
# sorted_numbers = sorted(numbers)

# # Displaying original and sorted lists
# print("Original List:", numbers)
# print("Sorted List: ", sorted_numbers)

# # Using for loop to iterate the sorted list
# print("\n Using for loop with sorted list: ")
# for num in sorted_numbers:
#     print(num, end = " ") 

#-------------------------------------
# numbers = [10,20,30,40,50]

# for n in numbers:
#     print(n)

# fruites = ["apple","Banana","Papaya"]

# for i in range(len(fruites)):
#     print(i, fruites[i])

#------------- Nested Loop

# for i in range(1,5):
#     for j in range(1,11):
#         result = i*j
#         print(f"{i}*{j} = {result}")

#---------- Pattern Building 
# n = int(input("Enter a number: "))
# for i in range(n+1):
#     print("*"*i)

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end = "")
#     print()

#----------Reverse traingle
# n = int(input("Enter a number: "))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end = "")
#     print()



#----------Number Traingle

# n = int(input("ENter a number: "))
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j, end = "")
#     print()

#------ Print the each element of the list: 
# list1 = [5,20,14,30,50,13, 3,9]

# for i in list1:
#     if i%2==0: 
#       print(i)


# ----------- Print the maximum number in a list (without using max()).
# list1 = [5,20,14,30,50,13, 3,9]

# max_number = list1[0]

# for n in list1:
#     if n>max_number:
#         max_number = n

# print("Maximum number is : ", max_number)
    

# for i in range(5):
#     for j in range(i):
#         print("*",end = "")
#     print()


#------------------------------
# names = ["Ram", "Shyam", "Subhash"]

# for i in names:
#     print(i,len(i))


#------------------------------
# numbers = [1,2,3,4,5,6,7,8,9]
# even_count = 0
# odd_count = 0

# for i in numbers:
#     if i%2==0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even Numbers Count: ", even_count)
# print("Odd Numbers Count: ", odd_count)


# ------------- Create this pattern
# 12345
# 1234
# 123
# 12
# 1


# for i in range(5,1,-1):
#     for j in range(i):
#         print(j, end = " ")
#     print()


# for i in range(4):
#     print("*"*4)


# Print this pyramid pattern:

#    *
#   ***
#  *****
# *******

# for i in range(6):
#     if i%2!=0:
#         print("*"*i, end= "")
#     print()
   

#---Mini Project: Student Marks Analyzer
''' 
marks = []
n = int(input("How many students numbers you want to enter: "))
print("*"*80)
for i in range(n):
    m = int(input(f"Enter {i+1}students marks: "))
    marks.append(m)


print("Marks: ", marks)
print("*"*80)
# Task: 
# Highet marks: 
highest_marks = marks[0]

for i in marks:
    if i > highest_marks :
        highest_marks = i

print("Highet Marks is: ", highest_marks)
print("*"*80)

# Lowest marks : 
lowest_marks = marks[0]

for i in marks:
    if i < lowest_marks:
        lowest_marks = i
print("Lowest makrs is: ", lowest_marks)
print("*"*80)
# Average marks: 
marks_sum = 0
for i in marks:
    marks_sum += i

average_marks = marks_sum/len(marks)
print("Average Makrs is: ", average_marks)
print("*"*80)
# Total : 
total = 0

for i in marks:
    total += i
print("Total is : ", total)
print("*"*80)  


# Count how many passed.
pass_student_count = 0 

for i in marks:
    if i>30:
        pass_student_count += 1

print("Pass Student Count: ", pass_student_count)
print("*"*80)
print("Thank you for using our service.")


'''
#---------------------
nums = [2, 4, 6, 8]
sum = 0

for n in nums:
    sum += n

print(sum)


#--------------
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()

#-----------
items = [10, 20, 30, 40]
max_num = items[0]

for x in items:
    if x > max_num:
        max_num = x

print(max_num)

#----------
marks = [50, 20, 70]
lowest = marks[0]

for m in marks:
    if m < lowest:
        lowest = m

print(lowest)

#------------
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()


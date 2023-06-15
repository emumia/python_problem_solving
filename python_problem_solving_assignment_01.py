#!/usr/bin/env python
# coding: utf-8

# In[8]:


# 1.Write a program to calculate the sum of two numbers.
print("Write a program to calculate the sum of two numbers.")

number1 = float(input("Enter First number here: "))
number2 = float(input("Enter Second number here: "))
sum_of_2_number = (number1 + number2)
print(f'sum of two number is: {int(sum_of_2_number)} and float answer is  {float(sum_of_2_number)} \n')


# In[11]:


# 2.Write a program to find the average of three numbers.

print("Write a program to find the average of three numbers.\n")

number1 = float(input("Enter First number here: "))
number2 = float(input("Enter Second number here: "))
number3 = float(input("Enter third number here: "))
average_of_3_number = (number1 + number2 + number3)/3
print(f'sum of two number is: {int(average_of_3_number)} and float answer is  {float(average_of_3_number)}')
print(f'sum of two number is in 2 decimal point: % .2f' %average_of_3_number)


# In[12]:


# 3.Write a program to check if a given number is even or odd.
print("Write a program to check if a given number is even or odd. \n")

number=int(input("Enter the number here: "))
if number %2 == 0:
    print(f"The number {number} is even ")
else:
    print(f"The number {number} is odd ")


# In[29]:


# 4.Write a program to find the maximum number among three given numbers.
num1=int(input("First number"))
num2=int(input("Second number"))
num3=int(input("Third number"))
largest_number=0

if num1>num2 and num1>num3:
    largest_number = num1
if num2 > num1 and num2 > num3:
    largest_number = num2
if num3 > num1 and num3 > num2:
    largest_number = num3
    
print(f"The largest number among three number is {largest_number} ")    


# In[43]:


# 5.Write a program to calculate the factorial of a given number.
num = int(input("Input number here: "))

factorial = 1

# checking if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print(f"The factorial of {num} is {factorial}")


# In[15]:


# 6.Check if a given number is even. Print True if it is, and False otherwise.
print("Check if a given number is even. Print True if it is, and False otherwise.\n")
number= int(input("Enter your number here: "))
if number %2 == 0:
    print("True")
else:
    print("False")


# In[33]:


# 7.Determine if a string contains only uppercase letters. Print True if it does, and False otherwise.
str1 = input("Enter string here: ")
if str1.isupper():
    print("True")
else:
    print("False")


# In[36]:


# 8.Given a list of integers, check if any of the numbers are negative. Print True if there is at least one negative number,
# and False otherwise.
print("Given a list of integers, check if any of the numbers are negative. Print True if there is at least one negative number, and False otherwise\n")
import numpy as np

# list of numbers
number1 = [-10, 21, 4, -45, -66, 93, -11]

# Using numpy to print the negative number
imran = np.array(number1)
negative_no = imran[imran <= 0]
if negative_no is not True:
    print("True,  There is negative number")
else:
    print("False,  there is negative number")

print("Negative numbers in the list: ", *negative_no)


# In[42]:


#easy way
 
# list of numbers
list1 = [11, -21, 0, 45, 66, -93]
 
# iterating each number in list
for num in list1:
    if num < 0:
        print("True")
        break


# In[37]:


# 9.Check if a given year is a leap year. Print True if it is, and False otherwise. Remember, a leap year is divisible by 
#4, but not divisible by 100, unless it is also divisible by 400.

year = int(input('Enter year here: '))   # To get year we are taking integer input from the user

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print(f"{year} is a leap year")

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print(f"{year} is not a leap year")


# In[38]:


#Another way to findout leap year
year = int(input("Enter year here:")) 
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} Leap year")
        else:
            print(f"{year} Not a leap year") 
    else:
          print(f"{year}Leap year") 
else:
    print(f"{year }Not a leap year")


# In[39]:


# 10.Given two strings, check if they have the same length. Print True if they do, and False otherwise.
print("Given two strings, check if they have the same length. Print True if they do, and False otherwise")

str1 = input("Enter your first string here: ")
str2 = input("Enter your first string here: ")
if len(str1) == len(str2):
    print("True")
else:
    print("False")


# In[ ]:





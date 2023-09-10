


import keyword
 


# printing all keywords at once using "kwlist()"


print("The list of keywords is : ")


print(keyword.kwlist)



# True, False, None Keyword


print (False == 0 )


print (True == 1 )



print (True + True + True)


print (True + False + False)



print (None == 0)


print (None == [])



# and, or, not, in, is


# showing logical operation on "or" (returns True)



print(True or False)


# showing logical operation on "and" (returns False)



print(False and True)
 


# showing logical operation on "not" (returns False)



print(not True)
 


# using "in" to check


if 's' in 'geeksforgeeks':

    print("s is part of geeksforgeeks")


else:

    print("s is not part of geeksforgeeks")
 


# using "in" for loop through


for i in 'geeksforgeeks':


    print(i, end=" ")


    print("\r")
 


# using is to check object identity


# string is immutable( cannot be changed once allocated)


# hence occupy same memory location


print(' ' is ' ')
 


# using is to check object identity


# dictionary is mutable( can be changed once allocated)


# hence occupy different memory location


print({} is {})



# for, while, break, continue



# Using for loop


for i in range(10):
 


    print(i, end=" ")
 


    # break the loop as soon it sees 6


    if i == 6:


        break
 
print()
 


# loop from 1 to 10


i = 0


while i < 10:
 


    # If i is equals to 6,


    # continue to next iteration


    # without printing


    if i == 6:


        i += 1
        continue


    else:


        # otherwise print the value
        # of i


        print(i, end=" ")
 


    i = i+1
    


    # if, else, and elif keyword
    


    i = 10


if (i == 10):


    print("i is 10")


elif (i == 20):


    print("i is 20")


else:
    print("i is not present")
    


    # def keyword
   


    def fun():


           print ("Inside Fun")
 
    fun()

    # Return and Yield Keyword
    

    # Return keyword

def fun():

    S = 0
 

    for i in range(10):

        S += i

    return S
 
 
print(fun())
 

# Yield Keyword
 
 

def fun():

    S = 0
 

    for i in range(10):

        S += i

        yield S
 
 

for i in fun():
    print(i)
    
    
# a class
 

class Dog:
 

    # A simple class

    # attribute

    attr1 = "mammal"

    attr2 = "dog"
 

    # A sample method

    def fun(self):

        print("I'm a", self.attr1)

        print("I'm a", self.attr2)
 
 

# Driver code

# Object instantiation

Rodger = Dog()
 

# Accessing class attributes

# and method through objects

print(Rodger.attr1)

Rodger.fun()



# using with statement

with open('file_path', 'w') as file:

    file.write('hello world !')
    
    # as use

    import math as gfg
 

print(gfg.factorial(5))


# Pass Keyword

n = 10

for i in range(n):
 

    # pass can be used as placeholder

    # when code is to added later
    pass


# Lambda keyword

g = lambda x: x*x*x
 

print(g(7))



# import keyword


from math import factorial

import math

print(math.factorial(10))
 

# from keyword

print(factorial(10))


 # try, except, raise, finally, and assert Keywords
 

# initializing number
a = 4
b = 0
 
# No exception Exception raised in try block
try:
    k = a//b  # raises divide by zero exception.
    print(k)
 
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
 
 # del keyword
my_variable1 = 20
my_variable2 = "GeeksForGeeks"
 
# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)
 
# delete both the variables
del my_variable1
del my_variable2
 
# check if my_variable1 and my_variable2 exists
#print(my_variable1)
#print(my_variable2)


# global variable
a = 15
b = 10
 
# function to perform addition
def add():
    c = a + b
    print(c)
 
# calling a function
add()
 
# nonlocal keyword
def fun():
    var1 = 10
 
    def gun():
        # tell python explicitly that it
        # has to access var1 initialized
        # in fun on line 2
        # using the keyword nonlocal
        nonlocal var1
         
        var1 = var1 + 10
        print(var1)
 
    gun()
fun()



# life time of a namespace
# var1 is in the global namespace
var1 = 5
def some_func():
 
    # var2 is in the local namespace
    var2 = 6
    def some_inner_func():
 
        # var3 is in the nested local
        # namespace
        var3 = 7

# Python program processing
# global variable
 
count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()

# Python program showing
# a scope of object
 
def some_func():
    print("Inside some_func")
    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:",var)
    some_inner_func()
  #  print("Try printing var from outer function: ",var)
some_func()


# Python indentation
 
site = 'gfg'
 
if site == 'gfg':
    print('Logging on to geeksforgeeks...')
else:
    print('retype the URL.')
print('All set !')

# another examlpe of identation


j = 1
while(j <= 5):
    print(j)
    j = j + 1
   
   
   # structuring the code in python 
    # Example 1
  
# The following code is valid
a = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
    ]
  
print(a)
    
# Example 2
# The following code is also valid
  
person_1 = 18
person_2 = 20
person_3 = 12
  
if (
   person_1 >= 18 and
   person_2 >= 18 and
   person_3 < 18
   ):
    print('2 Persons should have ID Cards')
    
    

# we can also code this in a different way
 
# Python code to demonstrate working of iskeyword()
 
# importing "keyword" for keyword operations
import keyword
# initializing strings for testing while putting them in an array
keys = ["for", "geeksforgeeks", "elif", "elseif", "nikhil",
        "assert", "shambhavi", "True", "False", "akshat", "akash", "break", "ashty", "lambda", "suman", "try", "vaishnavi"]
 
for i in range(len(keys)):
     # checking which are keywords
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is python keyword")
    else:
        print(keys[i] + " is not a python keyword")
        
        #assigning values to variables in Python 
        # initialising variable directly
        # for single value
a = 5
 
# printing value of a
print ("The value of a is: " + str(a))

# Assigning multiple values in single line
 
a,b,c="pak","vs","india"
print(a+b+c)

 
# Initialising variables using Conditional Operator for assigning values
a = 1 if 20 > 10 else 0
 
# Printing value of a
print("The value of a is: " , str(a))


# printing without newline in Python?

print("pak", end =" ")
print("pakistan")
 
# array
a = [1, 2, 3, 4]
 
# printing a element in same line
for i in range(4):
    print(a[i], end =" ")
    
    # using loop
    
    l = [1, 2, 3, 4, 5, 6]
 
# using * symbol prints the list
# elements in a single line
print(*l)


import sys
 
sys.stdout.write("pakistan ")
sys.stdout.write("Zindabad")

# Desion making
# python program to illustrate If statement
 
i = 10
 
if (i > 15):
    print("10 is less than 15")
print("I am Not in if")


# python program to illustrate If else statement
#!/usr/bin/python
 
i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")


# Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum
 
 
# Initializing list
List = [367, 111, 562, 945, 6726, 873]
 
# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]
 
# Displaying new list
print(newList)

# python program to illustrate nested If statement
 
i = 10
if (i == 10):
   
    #  First if statement
    if (i < 15):
        print("i is smaller than 15")
         
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
        
        
        # Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")

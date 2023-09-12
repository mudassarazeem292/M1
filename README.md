 # Python language introduction

Python is a general perpose language and it is easy like english language high level language used for machine learning ,web projects,AI and many other technologies #it have many build in libraries

# Python 3 basicss 
used for many applications #contains variable,data types,operators,data flow statements with extra features

# Python The new generation language

Python is widely used language due to its simplicity for scientific computing, data analysis, AI, web development, machine learning.
It has a number of features like interpreted,plateform independent,high level language,free and open source,easy to learn,scripting language,and build in library functions.

# What is Python3.0 and why we do programming?

It is an interpreted language which mean that everyone can read and execute the code
as it is used for developing websites,data analysis,data visualization and task automation which are used in programming

# Why Python is leading edge?

it is easy to learn having simplified syntax
free to use, large ecosystem of libraries and so beginers prefer to learn this language. 

# Whats the major difference between Python2.x and 3.x ?

Python 2 have more complicated syntax than python 3
libraries created by Python3 are more compatible to python3 which is not happened in Python2
Division operator
so difference occours in:

print function

Unicode

xrange

Error Handling

future module

# Keywords in Python | Set 1, Set 2

reserved values used as variable name ,function name ,or any other identifier
these are
### and
logical operator
### as
used to creat alia name
### assert
used for debugging
### break
to break a function
### class 
to define a class
### continue
skip the next iteration of loop
### define
to define a function
### del
to delete a function
### else 
for condition statement
### elif
also for conditional statement
### except
try except is used to handle these errors
### false
for false statement
### for
used for loop
### finaly
used with exception
### from
used for import specific part of module
### global 
for global variable
### if 
for conditional statement
### import
for importing a module
### is
to show that two variables are equal
### in
to check a value in a function
### lambda
to creat anonmyous function
### none
to check null value
### non local 
for non local variable
### not 
logical operator
### or 
logical operator
### pass 
used when a part we want not to execute
### raise
to raisa exception or error
### return
used for end the execution 
### true
represents an expression that will true
### try
used for handling eeror
### while
used to execute a block of statement
### with
used in exception handling
### yield
used to creat a generator function

# What is namespace:
these have a unique name for each object in Python. (variable or a method), Python itself maintains a namespace in the form of a Python dictionary. 

# Types of namespaces :

 The built-in namespace encompasses
the global namespace and
the global namespace encompasses the local namespace.

# What is Statement in Python
A Python statement is an instruction that the Python interpreter can execute.
# types of statements 
 Assignment statements, Conditional statements, Looping statements, etc.
# What is Indentation in Python
Whitespace is used for indentation in Python. Unlike many other programming languages which only serve to make the code easier to read
# What are Comments in Python
Python comments start with the hash symbol # and continue to the end of the line. Comments in Python are useful information that the developers provide to make the reader understand the source code. It explains the logic or a part of it used in the code. 
### Docstring in Python
Python Docstrings are a type of comment that is used to show how the program works. Docstrings in Python are surrounded by Triple Quotes in Python (“”” “””). Docstrings are also neglected by the interpreter.

# Structuring Python Programs
python statements can alter interpreter behavior like conditional statement

1-Implicit Line Continuation

This is the most straightforward technique in writing a statement that spans multiple lines.

2-Explicit Line Continuation

Explicit Line joining is used mostly when implicit line joining is not applicable. In this method, you have to use a character that helps the interpreter to understand that the particular statement is spanning more than one lines.

# Comments in Python
Writing comments in the code are very important and they help in code readability and also tell more about the code

### Whitespaces as Indentation
Python’s syntax is quite easy, but still you have to take some care in writing the code. Indentation is used in writing python codes.
# Structuring Python Programs
python statements can alter interpreter behavior like conditional statement

1-Implicit Line Continuation

This is the most straightforward technique in writing a statement that spans multiple lines.

2-Explicit Line Continuation

Explicit Line joining is used mostly when implicit line joining is not applicable. In this method, you have to use a character that helps the interpreter to understand that the particular statement is spanning more than one lines.

# Comments in Python
Writing comments in the code are very important and they help in code readability and also tell more about the code

### Whitespaces as Indentation
Python’s syntax is quite easy, but still you have to take some care in writing the code. Indentation is used in writing python codes.

## How to check if a string is a valid keyword in Python?
as kewards are reserving words How to check if a string is a keyword?

Python defines an inbuilt module “keyword” which handles certain operations related to keywords. A function “iskeyword()” checks if a string is a keyword or not. Returns true if a string is a keyword, else returns false. its code is given in py file

## How to assign values to variables in Python and other languages
in python no need to assign the values instead of c/c++ languages

so the method will be (given in code of single and muilti value assigning values)

direct assigning values

using operator 

## How to print without newline in Python?

in Python 3. x, you can use the end parameter of the print() function. as shown in code

by using for lop and sys module we can also do this

# Desion making
defines the direction of your code using if else

 we decide what should we do next..

 In Python programming language, the type of control flow statements is:

### The if statement

### The if-else statement

### The nested-if statement

### The if-elif-else ladder

# calculator using python
code in py file 

# python advantages and applications 
## advantages
Presence of third-party modules, having
Extensive support libraries(NumPy for numerical calculations, Pandas for data analytics, etc.) 
Open source and large active community base 
Versatile, Easy to read, learn and write
User-friendly data structures 
High-level language 
Dynamically typed language(No need to mention data type based on the value assigned, it takes data type) 
Object-Oriented and Procedural  Programming language
Portable and Interactive
Ideal for prototypes – provide more functionality with less coding
Highly Efficient(Python’s clean object-oriented design provides enhanced process control, and the language is equipped with excellent text processing and integration capabilities, as well as its own unit testing framework, which makes it more efficient.)
Internet of Things(IoT) Opportunities
Interpreted Language
Portable across Operating systems 

## application

GUI-based desktop applications,
Graphic design, image processing applications, Games, and Scientific/ computational Applications,
Web frameworks and applications ,
Enterprise and Business applications ,
Operating Systems ,
Education,
Database Access,
Language Development, 
Prototyping ,
Software Development,
 Data Science and Machine Learning,
Scripting.
# Taking input in Python
 Python provides two inbuilt functions to read the input from the keyboard. 
 

input ( prompt ),
raw_input ( prompt )
## How the input function works in Python : 
 

When input() function executes program flow will be stopped until the user has given input.
The text  displayed on the output screen to ask a user to enter an input value is optional i.e. the prompt, which will be printed on the screen is optional.
Whatever you enter as input, the input function converts it into a string. You need to explicitly convert it into an integer in your code using typecasting because input function convert integer to a string.


# Taking input from console in Python

### What is Console in Python? 
Console (also called Shell) is basically a command line interpreter that takes input from the user

### 1. Typecasting the input to Integer: 
There might be conditions when you might require integer input from the user/Console
### 2. Typecasting the input to Float:
 To convert the input to float the following code will work out. 
### 3. Typecasting the input to String:
 All kinds of input can be converted to string type whether they are float or integer.

## Python Input Methods for Competitive Programming

as python is a competitive language but slower tha other programming languages like java /C/C++ so to improve the speed of code execution for input/output intensive problems, languages have various input and output methods describe in code.

# Vulnerability in input() method

The vulnerability in input() method lies in the fact that the variable accessing the value of input can be accessed by anyone just by using the name of the variable or method. given in code of different types of vulnerability during raw_input

# Python | Output using print() function
### Python print() Function Syntax 
Syntax : print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

### Parameters: 

value(s): Any value, and as many as you like. Will be converted to a string before printed

sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘

end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’

file : (Optional) An object with a write method. Default :sys.stdout

flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

Return Type: It returns output to the screen.

# How to print without newline in Python?
Python has a predefined format if you use print(a_variable) then it will go to the next line automatically.
## Python end parameter in print()
By default Python‘s print() function ends with a newline.
## Python | sep parameter in print()
The separator between the arguments to print() function in Python is space by default (softspace feature) , which can be modified and can be made to any character, integer or string as per our choice. The ‘sep’ parameter is used to achieve this.

## Python | Output Formatting

In Python, there are several ways to present the output of a program. Data can be printed in a human-readable form, or written to a file for future use, or even in some other specified form. Users often want more control over the formatting of output than simply printing space-separated values.

Output Formatting in Python
### There are several ways to format output using String Method in Python. 

Using String Modulo Operator(%)

Using Format Method

Using The String Method

Python’s Format Conversion Rule

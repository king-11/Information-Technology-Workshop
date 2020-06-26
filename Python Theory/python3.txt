#Module: A collection of related functions, python definition and statements, that are placed in their own file.

# To import any module
import module_name

# To use any function from the module
module_name.function_name

Example:

import webbrowser
webbrowser.open("http://www.google.co.in")

Another way to use module:

from webbrowser import*
open("http://www.google.co.in")

Another way to use module:

from webbrowser import open as openWebsite
openWebsite("http://www.google.co.in")

#Creating and using a module:

def sayHi():                 # save as say_hi.py
    print("Hello Class")


import say_hi                #save as call_say_hi.py and run
say_hi.sayHi()

Output: Hello Class

Example:
# A simple module, calc.py 
  
def add(x, y): 
    return (x+y) 
  
def subtract(x, y): 
    return (x-y) 

# importing  module calc.py 
import calc 
  
print add(10, 2) 

# Fibonacci numbers module as fibo.py
Example:
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
#Now enter the Python interpreter and import this module with the following command:
>>>import fibo

#This does not enter the names of the functions defined in fibo directly in the current symbol table; it only enters the module name fibo there. Using the module name you can access the functions:
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#More in Module:
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

#If the module name is followed by as, then the name following as is bound directly to the imported module.
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

#It can also be used when utilising from with similar effects:
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
 
Standard Modules:

# importing sqrt() and factorial from the 
# module math 
from math import sqrt, factorial 

# if we simply do "import math", then 
# math.sqrt(16) and math.factorial() 
# are required. 
print sqrt(16) 
print factorial(6) 

#The dir() Function:

#The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:

>>> import math
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

#Python built-in-module:
# importing built-in module math 
import math 

# using square root(sqrt) function contained 
# in math module 
print (math.sqrt(25)) 

# using pi function contained in math module 
print (math.pi) 

# 1 * 2 * 3 * 4 = 24 
print (math.factorial(4)) 

#find the floating sum of a list
import math
value = [0.325, 1, 2]
result= math.fsum(value)
print(result)

# importing built in module random 
import random 

# printing random integer between 0 and 5 
print (random.randint(0, 5)) 

# print random floating point number between 0 and 1 
print (random.random()) 

# roll a die

import random
min =1; 
max =6;
result= random.randint(min, max)
print(result)

#print today's date and current time with date
import datetime
print(datetime.date.today())
print(datetime.datetime.now())

# Structure python module into packages

Create a folder name Package

def sayHi():              #save as say_hi.py in the folder Package
    print("Hello Class")

def gr(name):             #save as greeting.py in the folder Package
    print("Hi ", name)

Create a __init__.py file in the folder Package

from Packages.greeting import gr  #save as call_greet.py outside the folder Package
gr("Randheer")                    # run the file call_greet.py

Output: Hi Randheer 

from Packages.say_hi import sayHi
sayHi()

Output: Hello Class

#Input and Output

#There are several ways to present the output of a program; data can be printed in a human-readable form, or written to a file for future use. 

#want more control over the formatting of output. 

#The str() function = human-readable, while repr() generates representations which can be read by the interpreter.

#Examples:
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> #Example of repr()
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"

#The string module contains a Template class that offers yet another way to substitute values into strings, using placeholders like $x and replacing them with values from a dictionary, but offers much less control of the formatting.
#Formatted String Literals

#Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

#An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:

>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.


#The String format() Method
#Basic usage of the str.format() method looks like this:

>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"

#The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.

>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

#If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.

>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
Output: This spam is absolutely horrible.

#Positional and keyword arguments can be arbitrarily combined:

>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
Output: The story of Bill, Manfred, and Georg.

#Example using dict for output formating.

>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

#As an example, the following lines produce a tidily-aligned set of columns giving integers and their squares and cubes:

>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

#Manual String Formatting

#The str.rjust() method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left. There are similar methods str.ljust() and str.center(). These methods do not write anything, they just return a new string. 
#There is another method, str.zfill(), which pads a numeric string on the left with zeros. It understands about plus and minus signs:

>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'

#Old string formatting

#The % operator can also be used for string formatting. It interprets the left argument much like a sprintf()-style format string to be applied to the right argument, and returns the string resulting from this formatting operation. For example:

>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.

#Reading and Writing Files

#open() returns a file object, and is most commonly used with two arguments: open(filename, mode).

>>> f = open('workfile', 'w')


#It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:

>>> with open('workfile') as f:
...     read_data = f.read()
>>> f.closed
True
#write and read a file
f = open('workfile', 'w')
with open('workfile') as f:
    read_data = f.read()
a = f.closed
print(a)

#After a file object is closed, attempts to use the file object will automatically fail.

>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.

#Methods of File Objects

#The rest of the examples in this section will assume that a file object called f has already been created.

#reading a file line-by-line

with open('workfile') as f:
    read_data = f.readlines()
    #read_data = f.readline()
print(read_data)

#reading the lines:
with open('workfile') as f:
    for line in f:
        print(line, end='')












# IMPORTS
# ------------------------------------------------
# Python has many many classes already written that you can use
# To access methods and data from another class you must import it
import math
print(math.pi)       
>>> 3.141592653589793

import random
print(random.randint(1,5))   #any random number start from 1 and end with 5
>>> 3

# shorter version, using as to abbreviate module name
import math as m
print(m.pi)      
>>> 3.141592653589793

import random as rd
print(rd.randint(1,5))  #any random number start from 1 and end with 5
>>> 2

# import just one or two functions or constants rather than a whole module
# easier for coding, but need to beware names don't conflict
from math import pi
print(pi)          
>>> 3.141592653589793

from random import randint, shuffle
print(randint(1,5))                  
>>> 4
x = ['a', 'b', 'c'] 
>>>                 
shuffle(x)
>>>
print(x)                             
>>> ['b', 'c', 'a']

# can rename an imported function if you want
x = ['a', 'b', 'c']
from random import shuffle as sf
sf(x)
print(x)                             
>>> ['c', 'a', 'b']

# can also import whole module using *
from random import *
print(randint(1,5))                  
>>> 5


#Numpy
#------------------------------------------------------------
#Numpy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.

import numpy as np
>>>
a = np.array([1, 2, 3])   # Create a rank 1 array
>>>
print(type(a))            
>>>"<class 'numpy.ndarray'>"
print(a.shape)            
>>> "(3,)"
print(a[0], a[1], a[2])   
>>> "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)   
>>> "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
>>>
print(b.shape)                     
>>> "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   
>>> "1 2 4"

import numpy as np
>>>
a = np.zeros((2,2))   # Create an array of all zeros
>>>
print(a)             
>>> 
[[ 0.  0.]
 [ 0.  0.]]

b = np.ones((1,2))    # Create an array of all ones

print(b)              
>>>[[ 1.  1.]]

c = np.full((2,2), 7)  # Create a constant array
print(c)              
>>> 
[[ 7.  7.]
 [ 7.  7.]]

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)             
>>>
[[ 1.  0.]
 [ 0.  1.]]

e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     
>>>
[[ 0.91940167  0.08143941]
 [ 0.68744134  0.87236687]]

import numpy as np
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
>>> 219
print(np.dot(v, w))     # using numpy library
>>> 219

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
>>> [29 67]
print(np.dot(x, v))
>>> [29 67]

# Matrix / matrix product; both produce the rank 2 array
print(x.dot(y))
>>>
[[19 22]
 [43 50]]

print(np.dot(x, y))
>>>
[[19 22]
 [43 50]]

import numpy as np

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)
>>>
[[ 2  2  4]
 [ 5  5  7]
 [ 8  8 10]
 [11 11 13]]

#Pandas
#------------------------------------------------------------------------
#Pandas is the most popular python library that is used for data analysis. It provides highly optimized performance with back-end source code.

# Program to Create series with scalar values 
import pandas as pd
Data =[1, 3, 4, 5, 6, 2, 9] # Numeric data 

# Creating series with default index values 
s = pd.Series(Data)	 

# predefined index values 
Index =['a', 'b', 'c', 'd', 'e', 'f', 'g'] 

# Creating series with predefined index values 
si = pd.Series(Data, Index) 
print(si)
>>>
a    1
b    3
c    4
d    5
e    6
f    2
g    9
dtype: int64

import pandas as pd
# Program to Create Dictionary series 
dictionary ={'a':1, 'b':2, 'c':3, 'd':4, 'e':5} 

# Creating series of Dictionary type 
sd = pd.Series(dictionary) 
print(sd)
>>>
a    1
b    2
c    3
d    4
e    5
dtype: int64

# Program to Create ndarray series 
import pandas as pd
Data =[[2, 3, 4], [5, 6, 7]] # Defining 2darray 

# Creating series of 2darray 
snd = pd.Series(Data)	 
print(snd)
>>>
0    [2, 3, 4]
1    [5, 6, 7]
dtype: object

# Program to create Dataframe of three series 
import pandas as pd 
s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])		 # Define series 1 
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])   # Define series 2 
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])	 # Define series 3 
Data ={'first':s1, 'second':s2, 'third':s3}      # Define Data 
dfseries = pd.DataFrame(Data)			 # Create DataFrame 
print(dfseries)
>>>
   first  second third
0      1     1.1     a
1      3     3.5     b
2      4     4.7     c
3      5     5.8     d
4      6     2.9     e
5      2     9.3   NaN
6      9     NaN   NaN

# importing pandas package
import pandas as pd
# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")
# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first, "\n", second)
>>>
Team        Boston Celtics
Number                   0
Position                PG
Age                     25
Height                 6-2
Weight                 180
College              Texas
Salary         7.73034e+06
Name: Avery Bradley, dtype: object 
 Team        Boston Celtics
Number                  28
Position                SG
Age                     22
Height                 6-5
Weight                 185
College      Georgia State
Salary         1.14864e+06
Name: R.J. Hunter, dtype: object

# Checking for missing values using isnull() and notnull():
import pandas as pd
# importing numpy as np
import numpy as np
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
# creating a dataframe from list
df = pd.DataFrame(dict)
# using isnull() function  
a = df.isnull()
print(df, "\n\n", a)
>>>
   First Score  Second Score  Third Score
0        100.0          30.0          NaN
1         90.0          45.0         40.0
2          NaN          56.0         80.0
3         95.0           NaN         98.0 

    First Score  Second Score  Third Score
0        False         False         True
1        False         False        False
2         True         False        False
3        False          True        False

#Matplotlib
#------------------------------------------------------------------------------
#Matplotlib is an amazing visualization library in Python for 2D plots of arrays.
#Matplotlib consists of several plots like line, bar, scatter, histogram etc.

#line plot
# importing matplotlib module 
from matplotlib import pyplot as plt 
# x-axis values 
x = [5, 2, 9, 4, 7] 
# Y-axis values 
y = [10, 5, 8, 4, 2] 
# Function to plot 
plt.plot(x,y) 
# function to show the plot 
plt.show() 

#bar graph
# importing matplotlib module 
from matplotlib import pyplot as plt 
# x-axis values 
x = [5, 2, 9, 4, 7] 
# Y-axis values 
y = [10, 5, 8, 4, 2] 
# Function to plot the bar 
plt.bar(x,y) 
# function to show the plot 
plt.show() 

#Scatter plot
# importing matplotlib module 
from matplotlib import pyplot as plt 
# x-axis values 
x = [5, 2, 9, 4, 7] 
# Y-axis values 
y = [10, 5, 8, 4, 2] 
# Function to plot scatter 
plt.scatter(x, y) 
# function to show the plot 
plt.show() 


# FILE READ & WRITE
# ------------------------------------------------
filename = 'city_data.txt'

# this opens a file handle called fin, iterates the lines of the file, and prints each line
with open(filename) as fin:
    for line in fin:
        print(line)
>>>
Country Code,Country Name,City Name,City Population

08,US,San Jose,70

09,Canada,Vancouver,30

08,US,San Francisco,90

07,China,Beijing,40

# we can grab words from a line by using split, which turns each line into a list called row

filename = 'city_data.txt'
with open(filename) as fin:
    fin.readline()
    for line in fin:
        row = line.split(',')
        print('Country:', row[1], ' City:', row[2])
>>>
Country: US  City: San Jose
Country: Canada  City: Vancouver
Country: US  City: San Francisco
Country: China  City: Beijing

# use the w parameter to write to an output file
filename = 'city_data.txt'
with open('Cities.txt', 'w') as fout:
    with open(filename) as fin:
        fin.readline()
        for line in fin:
            row = line.split(',')
            fout.write(row[2] + '\n')

>>>
San Jose
Vancouver
San Francisco
Beijing


# CLASSES & OBJECTS
# ------------------------------------------------
# Use classes to model real-world things. 
# Keep related data (variables) and actions (functions) in one block of code.
class Circle:
	# Circle constructor -- __init__ method creates a new Circle object
	def __init__(self, r = 1):
		self.radius = r
		
	def getPerimeter(self):
		return 2 * self.radius * 3.14
		
	def getArea(self):
		return self.radius ** 2 * 3.14
# all methods have the self parameter, which is Python's reference to the object that invoked the method

# this calls the __init__ method, which creates the new Circle
circle1 = Circle(3)		
# you can access the circle's attributes and methods using the dot operator
print("Radius =", circle1.radius)             
>>> Radius = 3
print("Perimeter =", circle1.getPerimeter())  
>>> Perimeter = 18.84


# FUNCTIONS
# ------------------------------------------------
# use the def keyword to create a function
# give the function a name, followed by parentheses and a colon
# you can pass in 0 or more variables. here we pass in num.
# you can return 0 or more variables. here we return the cube of num
# indention is important.
def cuber(num):
	num_cubed = num * num * num
	return num_cubed
# to call the function, and pass in 5:
a = cuber(5)
print(a)
>>> 125

# but if you want to assign the return value (125) to a variable,
x = 5
x_cubed = cuber(x)
print(x, x_cubed)
>>> 5 125

# you can set default values for parameters
def cuber(num = 2):
	num_cubed = num * num * num
	return num_cubed
	
print(cuber())	  # uses the default 2
>>> 8
print(cuber(3))	  # 3 overrides the default
>>> 27

# you can pass in multiple values, and return multiple values
# but order is important
def solve_triangle(base, height, side1, side2, side3):
	area = base * height / 2
	perimeter = side1 + side2 + side3
	return area, perimeter
	
area, perim = solve_triangle(3, 4, 5, 3, 4)	# b=3, h=4, s1=5, s2=3, s3=4
print('Area:', area, ' Perimeter:', perim)
>>> Area: 6.0  Perimeter: 12

# above are all called "positional arguments", and order matters
# you can also pass in "keyword arguments" when calling a function
a, p = solve_triangle(side1=5, side2=3, side3=4, height=4, base=3)
print(a, p)
>>> 6.0 12

# or use a combination of both, but positional arguments must come first
a, p = solve_triangle(3, 4, side3=4, side2=3, side1=5)
print(a, p)
>>> 6.0 12
	

# DATA STRUCTURES
# ------------------------------------------------
# These functions all work on String, List, and Tuple

# Indexing -- access any item in the sequence using its index
x = 'frog'
>>>
print (x[3])			 
>>> 'g'

x = ['pig', 'cow', 'horse']
>>>
print (x[1])			
>>> 'cow'

# Slicing -- slice out substrings, sublists, subtuples using indexes
# [start : end+1 : step]
x = 'computer'
>>>
print(x[1:4])			# items 1 to 3 
>>> 'omp'
print(x[1:6:2])			# items 1, 3, 5
>>> 'opt'
print(x[3:])			# items 3 to end
>>> 'puter'
print(x[:5])			# items 0 to 4
>>> 'compu'
print(x[-1])			# last item
>>> 'r'
print(x[-3:])			# last 3 items
>>> 'ter'
print(x[:-2])			# all except last 2 items
>>> 'comput'

# Adding / Concatenating -- combine 2 sequences of the same type using +
x = 'horse' + 'shoe'
>>>
print (x)				
>>> 'horseshoe'	

x = ['pig', 'cow'] + ['horse']
>>>
print (x)				
>>> ['pig', 'cow', 'horse']

# Multiplying -- multiply a sequence using *
x = 'bug' * 3
>>>
print (x)				
>>> 'bugbugbug'

x = [8, 5] * 3
>>>
print (x)				
>>> [8, 5, 8, 5, 8, 5]

# Checking Membership -- test whether an item is in or not in a sequence
x = 'bug'
>>>
print ('u' in x)		
>>> True

x = ['pig', 'cow', 'horse']
>>>
print ('cow' not in x)	        
>>> False

# Iterating	-- iterate through the items in a sequence
x = [7, 8, 3]
for item in x:
	print (item * 2)	
>>> 14, 16, 6
	
x = [7, 8, 3]
for index, item in enumerate(x):
	print (index, item)	
>>>
0 7
1 8
2 3

# Length -- count the number of items in a sequence
x = 'bug'
>>>
print (len(x))			
>>> 3

x = ['pig', 'cow', 'horse']
>>>
print (len(x))			
>>> 3

# Minimum -- find the minimum item in a sequence lexicographically
# alpha or numeric types, but cannot mix types
x = 'bug'
>>>
print (min(x))			
>>> 'b' 

x = ['pig', 'cow', 'horse']
>>>
print (min(x))			
>>> 'cow'

# Maximum -- find the maximum item in a sequence
# alpha or numeric types, but cannot mix types
x = 'bug'
>>>
print (max(x))			
>>> 'u' 

x = ['pig', 'cow', 'horse']
>>>
print (max(x))			
>>> 'pig'

# Sum -- find the sum of items in a sequence
# entire sequence must be numeric type
x = [5, 7, 'bug']
>>>
print (sum(x))			
>>> error!

x = [2, 5, 8, 12]
print (sum(x))			# prints 27
print (sum(x[-2:])) 	        # prints 20	

# Sorting -- returns a new list of items in sorted order

# sorted does not change the original list
x = 'bug'
>>>
print (sorted(x))	    
>>> ['b', 'g', 'u']

x = ['pig', 'cow', 'horse']
>>>
print(sorted(x))	    
>>> ['cow', 'horse', 'pig']

# count (item)	
# Returns count of an item
x = 'hippo'
>>>
print(x.count('p'))	
>>> 2

x = ['pig', 'cow', 'horse', 'cow']
>>>
print(x.count('cow'))	
>>> 2

# index (item)	
# Returns the index of the first occurrence of an item
x = 'hippo'
>>>
print (x.index('p'))   # index of first p	
>>> 2

x = ['pig', 'cow', 'horse', 'cow']
>>>
print (x.index('cow'))	
>>> 1

# Unpacking	- unpack the n items of a sequence into n variables
x = ['pig', 'cow', 'horse']
>>>
a, b, c = x
>>>
print(a)
>>> 'pig'
print(b)
>>> 'cow'
print(c) 
>>> 'horse'           

# LISTS
# ------------------------------------------------
# constructors – creating a new list
x = list((1, 2, 3))    # note double parens
>>>
x
>>> [1, 2, 3] 
x = ['a', 25, 'dog', 8.43] 
>>>
x
>>> ['a', 25, 'dog', 8.43]

# list creation using comprehensions
x = [m for m in range(8)]   
>>> [0, 1, 2, 3, 4, 5, 6, 7]

x = [z**2 for z in range(10) if z>4]
>>> [25, 36, 49, 64, 81]

# Delete -- delete a list or an item from a list
x = [5, 3, 8, 6]
>>>
del(x[1])				
>>> [5, 8, 6]
del(x)		# deletes list x

# Append -- append an item to a list
x = [5, 3, 8, 6]
>>>
x.append(7)				
>>> [5, 3, 8, 6, 7]

# Extend -- append an sequence to a list
my_list = ['Hello', 'for', 0, 0, 7] 
my_list.extend(['ITW1']) 
print(my_list)  	
>>> ['Hello', 'for', 0, 0, 7, 'ITW1']

# Insert -- insert an item at given index.	
# x.insert(index, item)
x = [5, 3, 8, 6]
>>>
x.insert(1, 7)		
print(x)
>>> [5, 7, 3, 8, 6]
x.insert(1,['a','m'])	
print(x)
>>> [5, ['a', 'm'], 7, 3, 8, 6] 

# Pop -- pops last item off the list, and returns item
x = [5, 3, 8, 6]
>>>
x.pop()
>>> 6
print(x)	        
>>> [5, 3, 8]			
x.pop()
>>> 8
print(x)                
>>> [5, 3]

# Remove -- remove first instance of an item
x = [5, 3, 8, 6, 3]
>>>
x.remove(3)	
>>> 
print(x)
>>> [5, 8, 6, 3]

x = [5, 3, 8, 6, 3]
>>>
x.remove(x[1])    
>>>
print(x)
>>> [5, 8, 6, 3]

# Reverse -- reverse the order of the list
x = [5, 3, 8, 6]
>>>
x.reverse()
>>>
print(x)
>>> [6, 8, 3, 5]

# Sort -- sort the list in place
# sorted(x) returns a new sorted list without changing the original list x. 
# x.sort() puts the items of x in sorted order (sorts in place).
x = [5, 3, 8, 6]
>>>
x.sort()
>>>
print(x)
>>> [3, 5, 6, 8]

# Clear	-- delete all items from the list
x = [5, 3, 8, 6]
>>>
x.clear()
>>>
print(x)
>>> []

# TUPLES
# ------------------------------------------------
# constructors – creating a new tuple
x = ()					# no-item tuple
x = (1,2,3)
x = 1, 2, 3				# parenthesis are optional
x = 2, 					# single-item tuple
list1 = [5, 7, 7]                       # list
>>>
x = tuple(list1)		        # tuple from list
>>>
print(x)
>>> (5, 7, 7)
# Tuples are Immutable, but member objects may be mutable
x = (1, 2, 3)
>>>
del(x[1])
>>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion

x[1] = 8				
>>> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

x = ([1,2], 3)			# 2-item tuple: list and int
>>>
print(x)
>>> ([1, 2], 3)
del(x[0][1])
>>>
print(x)			
>>> ([1], 3)

# SETS
# ------------------------------------------------
# constructors – creating a new set
x = {3,5,3,5}
>>>
print(x)			
>>> {3, 5}

x = set()
>>>
print(x)			
>>> set()  # empty set
list1 = [5, 7, 7]
>>>
x = set(list1)			# new set from list. strips duplicates
>>> {5, 7}

# Set Comprehension
x = {3*x for x in range(10) if x>5}
>>>
print(x)
>>> {18, 21, 24, 27}            # but in random order

# DICTIONARIES
# ------------------------------------------------
# constructors – creating a new dict
x = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
>>>
x = dict([('pork', 25.3),('beef', 33.8),('chicken', 22.7)])
>>>
x = dict(pork=25.3, beef=33.8, chicken=22.7)
>>>
print(x)
>>> {'chicken': 22.7, 'pork': 25.3, 'beef': 33.8}

# Accessing keys and values in a dict
x.keys()           # returns list of keys in x
>>> dict_keys(['pork', 'beef', 'chicken'])	
			
x.values()	   # returns list of values in x
>>> dict_values([25.3, 33.8, 22.7])

x.items()	   # returns list of key-value tuple pairs in x
>>> dict_items([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])

# Iterating a Dict
x = dict(pork=25.3, beef=33.8, chicken=22.7)
for key in x:		# iterate keys
    print(key, x[key])	# print all key/value pairs
>>>
pork 25.3
beef 33.8
chicken 22.7

for k, v in x.items():	# iterate key/value pairs
    print(k, v)		# print all key/value pairs
>>>
pork 25.3
beef 33.8
chicken 22.7


# INTRODUCTION TO BASIC PYTHON
# ------------------------------------------------
# to print, put text inside single or double quotes, inside parentheses.
print('Hello World')   
>>> Hello World
# VARIABLES 
# ------------------------------------------------
# variables are used for temporary storage of data that may change
# a single equals sign is the assignment operator
age = 26
>>>
first_name = 'Shiva'
>>>
gpa = 3.99
>>>

# here we can see three different types of data stored in variables: an integer, a string, and a float.
# You do not have to declare the data type stored in each variable. Python does that for you.
# You can see what type of data is in a variable using the type() function

print(type(age))          
>>> <class 'int'>
print(type(first_name))   
>>> <class 'str'>
print(type(gpa))          
>>> <class 'float'>

# variables are "dynamically typed" -- Python checks the type at runtime

age = 27.2              
>>>
print(type(age))        
>>> <class 'float'>
print(age, type(age))   
>>> 27.2 <class 'float'>

# variable naming tips: 
#	naming can have letters, numbers and underscore, but cannot start with a digit
#	some Python reserved words cannot be used
#	use descriptive variable names
#	Case Matters
#	constants in all caps: PI = 3.14159
# every Python variable is a pointer to the data stored somewhere in memory
# get memory location of a variable using id() function
print(id(age))    # Memory Location
>>> 140337655201584
# to swap variable values:
x = 5
>>>
y = 10
>>>
x, y = y, x
>>>
print('x =', x, 'y =', y)
>>> x = 10 y = 5

# BOOLEAN VALUES - True or False
# ------------------------------------------------
# These all evaluate to False: 0, 0.0, [], "", None
# These are all True: any non-zero number, any non-empty string, list or set
print(bool(1))      
>>> True
print(bool('dog'))  
>>> True
print(bool(10.78))  
>>> True
print(bool(0 or 1)) 
>>> True

print(bool(0))    
>>> False
print(bool(''))   
>>> False
print(bool(0 and 1))  
>>> False

# MATH FUNCTIONS
# ------------------------------------------------
# built-in arithmetic functions are: add, subtract, multiply, divide, power, integer division, and modulus (AKA: mod or remainder)
#	+  Addition
# 	-  Subtraction
# 	*  Multiplication
# 	/  Division
# 	// Integer Division
# 	%  Modulus (division remainder)
# 	** Power
x = 5 + 7
>>>
print(x, type(x))
>>> 12 <class 'int'>

x = 5 - 7
>>>
print(x, type(x))
>>> -2 <class 'int'>

x = 7 / 4
>>>
print(x, type(x))
>>> 1.75 <class 'float'>

x = 7 // 4
>>>
print(x, type(x))
>>> 1 <class 'int'>

x = 7 % 4
>>>
print(x)
>>> 3

x = 4 ** 3
>>>
print(x)
>>> 64

# x += 5 is the same as saying x = x + 5
x = 2
>>>
x = x + 5
>>>
print(x)   
>>> 12 <class 'int'>

x = 2
>>>
x += 5
>>>
print(x)   
>>> 7

# Order of Operations
#	1. ( )
#	2. **
#	3. * / // %
#	4. + -
#	Example: 1 + 5 ** (3 // 2) - 6 % 4 => 4
x = 1 + 5 ** (3 // 2) - 6 % 4
>>>
print(x)   
>>> 4

# CONSOLE INPUT
# ------------------------------------------------
# Get user input from the keyboard at the command prompt
name = input('What is your name? ')
>>> What is your name? Raj
print("Hello,", name)
>>> What is your name? Raj
age = eval(input('How old are you? '))
>>> How old are you? 27
print('Age =', age, type(age))
>>> Age = 27 <class 'int'>

# With what we know so far we can write a program to get user input and compute the area of a triangle.
base = eval(input('Enter the base: '))
>>> Enter the base: 10
height = eval(input('Enter the height: '))
>>> Enter the height: 15
area = base * height / 2
>>>
print('Area = ', area)
>>> Area =  75.0

# COMMENTS
# ------------------------------------------------
# Hash tag for single line comment
'''Three sets of quotes for multi-line comments'''
>>> 'Three sets of quotes for multi-line comments'

""" double quotes work too """
>>> ' double quotes work too '

# IF-ELIF-ELSE STATEMENTS
# ------------------------------------------------
# requires a boolean expression 
x = 69
>>>
print(x > 50)   
>>> True
print(x == 50)  
>>> False
print(x != 50)  
>>> True

my_age = 19
print(my_age > 21)
if my_age >= 21:
    print("Old enough.")
else:
    print("Not old enough.")
    print("Maybe next year.")

>>> False
>>> Not old enough.
>>> Maybe next year.

score = 72
if score > 90:
    print('Grade: A')
elif score > 80:
    print('Grade: B')
elif score > 70:
    print('Grade: C')
elif score > 60:
    print('Grade: D')
else:
    print('Grade: F')

>>> Grade: C
	
# can have multiple conditions in an if, using and/or
my_age = 19
grade = 'C'
if my_age > 18 and grade == 'A':
    print('I can go to the party!')
else:
    print('I can not go for the party')

>>> I can not go for the party

# nested if statements -- both conditions must be True
my_age = 19
grade = 'C'
if my_age > 18:
    if grade == 'A':
        print('I can go to the party!')
    else:
        print('I can not go for the party')

>>> I can not go for the party

# if ternary
x = 10
>>>
y = 20
>>>
#  action/ if condition true/ else condfition false
z = x + y if x > y else y - x
>>>
print(z)
>>> 10

# STRINGS
# ------------------------------------------------
# a string is a sequence of characters (ie. text)
s = 'Howdy'
>>>
print(s)                 
>>> Howdy
print(len(s))            
>>> 5
print(s[3])              
>>> d
print(s[1:3])           
>>> ow
t = ' dude! '
>>>
s += t
>>>
print(s + '|')         
>>> Howdy dude! |
print(s.strip() + '|') #remove all the leading and trailing spaces from a string
>>> Howdy dude!| 
s = s.rstrip('! ')     # delete all the trailing characters mentioned in its argument
print(s)               
>>> Howdy dude

s = 'Howdy dude!'
>>>
print(s.lower())                       
>>> howdy dude!
print(s.upper()[:5])                   
>>> HOWDY
print(s.title())                       
>>> Howdy Dude!
print(s.replace('Howdy', 'Greetings')) 
>>> Greetings dude!
print(s)                               
>>> Howdy dude!
print(s.count('d'))                    
>>> 3
print(s.find('w'))                     # index of 'w'
>>> 2 
print('dud' in s)                      # check the membership.
>>> True
print('X' not in s)                    # check the membership.
>>> True
print(s.startswith('How'))             
>>> True
print(s.endswith('cat'))               
>>> False
print(s > 'Honk')                      
>>> True
print(s.isalpha()) #returns “True” if all characters in the string are alphabets.
>>> False
print(s[0:4].isalpha())                
>>> True
print(s.isnumeric())                   
>>> False

print(s.split())              # split by space
>>> ['Howdy', 'dude!']
print('5,7,9'.split(','))     # split by comma
>>> ['5', '7', '9']
print('73.294'.split('.'))    # split by dot
>>> ['73', '294']
print(s[0], '\t', s[1], '\t', s[2])  # accessing using index number
>>> H        o       w
# LOOPS -- FOR, WHILE
# ------------------------------------------------
# used to iterate through the items of a string or list
# indention is important. 
# every statement indented from for will be executed each iteration
s = 'Raj'
for letter in s:
    print(letter)
for letter in s:
    print(letter, end='')
>>>> 
R
a
j
Raj

# if inside a for loop. indention is important.
for p in s:
    if p != 'a':
        print(p, end='')  
>>> Rj

for i in range(len(s)):
    print(i, end='')      

>>> 012

for i in range(len(s)):
    print(s[i])
for i in range(len(s)-1, -1, -1):
    print(s[i])
print(s[::-1])

>>>>
R
a
j
j
a
R
jaR

# while loops are an alternative to for loops
# they check a boolean each iteration, and exit the loop when the bool is False
x = 2
while x < 5:
    print('ha')
    x += 1
>>>
ha
ha
ha



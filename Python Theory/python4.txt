#Python program terminates as soon as it encounters an error. In Python, an error can be a syntax error or an exception.
# Syntax Error (also known as parsing errors):
# Errors caused by not following the proper structure (syntax) of the language are called syntax error.
#The parser repeats the line on which the error is and displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected. The error is caused by (or at least detected at) the token preceding the arrow.
#Syntax errors are easy to fix, Python will show you the line number where the error is, with an error message which will be self-explanatory.
Examples:
#Syntax Error
>>> print( 0 / 0 ))
  File "<stdin>", line 1
    print( 0 / 0 ))
                  ^
SyntaxError: invalid syntax
#The arrow indicates where the parser ran into the syntax error.
#Exception Error: Errors can also occur at runtime and these are called exceptions.This type of error occurs whenever syntactically correct Python code results in an error.
#Whenever these type of runtime error occur, Python creates an exception object. If not handled properly, it prints a traceback to that error along with some details about why that error occurred.
>>> print( 0 / 0 )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
Example:
>>> open("imaginary.txt")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary.txt'
#There are plenty of built-in exceptions in Python that are raised when corresponding errors occur.
#When these exceptions occur, it causes the current process to stop and passes it to the calling process until it is handled. If not handled, our program will crash.
# To handle the exception we use three blocks, named as:
1. try     #lets you test a block of code for errors.

2. except  #lets you handle the error.

3. finally #lets you execute code, regardless of the result of the try- and except block
Examples:

try:
  print(x)
except:
  print("An exception occurred")

Output:An exception occurred. #because x is not defined.

#Since the try block raises an error, the except block will be executed.
#Without the try block, the program will crash and raise an error.

print(x) #raise an error(NameError), because x is not defined.

#Many Exceptions:
#You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error.

try:
  print(x)                            # x is not defined.
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

Output: Variable x is not defined.

try:
  print(x)
  print(0/0)
except NameError:
  print("Variable x is not defined")
except ZeroDivisionError:
  print("division by zero")
except:
  print("Something else went wrong")

Output: Variable x is not defined

#else

try:
  print("Hello")  
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#try block does not raise any errors, so the else block is executed.
Output: Hello
        Nothing went wrong

#finally

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

Output: Something went wrong
        The 'try except' is finished 

try:
  print("x")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")

Output: x
        Nothing went wrong
        The 'try except' is finished

try:
  f = open("myfile.txt")
  f.write("ITW1 Classes")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

#try block will raise an error when trying to write to a read-only file.

Output: Something went wrong when writing to the file. 


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")

Output: result is 2.0
        executing finally clause
        division by zero!
        executing finally clause
        executing finally clause
        TypeError: unsupported operand type(s) for /: 'str' and 'str'

#Raising Exceptions
# The raise statement allows the programmer to force a specified exception to occur. 

raise NameError('HiThere')

Output: Traceback (most recent call last):
        File "<ipython-input-40-93385ba972b1>", line 1, in <module>
        raise NameError('HiThere')

        NameError: HiThere
# The sole argument to raise indicates the exception to be raised.

#If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception.
Example:
try:
    raise NameError('Hi ITW1!')
except NameError:
    print('An exception flew by!')
    raise

Output: An exception flew by!
        Traceback (most recent call last):
        File "<stdin>", line 2, in <module>
        NameError: Hi ITW1!

#Classes:
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#Class: It is define as the prototype of object. It provides bundling of data and function.
#Method: function define within the class.
#Instantiation: Creating a instance of specific class.
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#The __init__() function is called automatically every time the class is being used to create a new object.
#How to create a class:
Example: Let we have a class named as Car. The class Car have different-different cars, each of them are differe to each other by their attributes like make(registration no.), model(model no.), year(i.e. 2019) etc.

class Car:
    """Name of the class is Car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print("Instance object of the class is created")
        
    def displayParameters(self):
        print("Make: ", self.make)
        print("Model ", self.model)
        print("Year ", self.year)
        print()

#Creating objcet: object_name = class_name(parameters)

class Car:
    """Name of the class is Car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print("Instance object of the class is created")
        
    def displayParameters(self):
        print("Make: ", self.make)
        print("Model ", self.model)
        print("Year ", self.year)
        print()
        
car1 = Car("A", "B", 2019)  #object_name = class_name(parameters)

Output: Instance object of the class is created

#Accessing Member: object_name.member_name

class Car:
    """Name of the class is Car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print("Instance object of the class is created")
        
    def displayParameters(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print()
        
car1 = Car("A", "B", 2019)
car1.displayParameters()   #object_name.member_name
car2 = Car("C", "D", 2017)
car2.displayParameters()

Output: Instance object of the class is created
        Make:  A
        Model:  B
        Year:  2019

        Instance object of the class is created
        Make:  C
        Model:  D
        Year:  2017

Example:

class Car:
    """Name of the class is Car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print("Instance object of the class is created")
        
    def displayParameters(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print()
        
car1 = Car("A", "B", 2019)
print(car1.make)
car2 = Car("C", "D", 2017)
print(car2.make)

Output: Instance object of the class is created
        A
        Instance object of the class is created
        C
#Class variable: class_name.variable_name

class Car:
    """Name of the class is Car"""
    totalNumber = 0
    def __init__(self, make, model, year):
        Car.totalNumber+=1 
        self.make = make
        self.model = model
        self.year = year
        
        
    def displayParameters(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print()
        
car1 = Car("A", "B", 2019)
car2 = Car("C", "D", 2017)
car3 = Car("E", "F", 2015)
car4 = Car("G", "H", 2013)
print("Total no. of cars are:", Car.totalNumber)

Output: Total no. of cars are: 4

#Garbage Collection: del object_name

class Car:
    """Name of the class is Car"""
    totalNumber = 0
    def __init__(self, make, model, year):
        Car.totalNumber+=1 
        self.make = make
        self.model = model
        self.year = year
        
    def __del__(self):
        Car.totalNumber-=1
        
    def displayParameters(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print()
        
car1 = Car("A", "B", 2019)
car2 = Car("C", "D", 2017)
car3 = Car("E", "F", 2015)
car4 = Car("G", "H", 2013)

del car4
print(car1.make)

Output: A

#Inheritance: Child class is derived from parent class.

class ChildClass(ParentClass):
      code

      OR

class SubClass(SuperClass):
      code

Example:

class Car:
    superString = "Class variable is super clsss"
    def __init__(self):
        print("Initialization method of super class is called")
    def superMethod(self):
        print("Method of super calss is called")
        
class LuxeriousCar(Car):
    subString = "Class variable of sub class"
    def __init__(self):
        print("Initialization method of sub class is called")
    def subMethod(self):
        print("Method of sub calss is called")
        
subCar = LuxeriousCar()
subCar.superMethod()
print(subCar.superString)
print(subCar.subString)

Output: Initialization method of sub class is called
        Method of super calss is called
        Class variable is super clsss
        Class variable of sub class

#subclass of subclass:

class Car:
    superString = "Class value of car"
    def __init__(self):
        print("Instance object of car is created")
    def superMethod(self):
        print("Method of car is called")
        
class LuxeriousCar(Car):
    subString = "Class variable of LuxeriousCar"
    def __init__(self):
        print("Instance object of LuxeriousCar is created")
    def subMethod(self):
        print("Method of LuxeriousCar is called")
        
class SubLuxeriousCar(LuxeriousCar):
    def __init__(self):
        print("Instance object of SubLuxeriousCar is created")
        
subSubCar = SubLuxeriousCar()
subSubCar.superMethod()
subSubCar.subMethod()

Output: Instance object of SubLuxeriousCar is created
        Method of car is called
        Method of LuxeriousCar is called



















       



































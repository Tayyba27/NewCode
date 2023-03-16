# Python & Files

# %%
# working with files in python(the building function open)
#using it in the context in ML DL and AI

# %%

# im done alhudulillah
x = open(r"C:\Users\3\Desktop\Test.txt","r")


# %% [markdown]
# # Importing code in python

# %%
import math

# %%
math.sqrt(5)

# %%
math.sinh(100)

# %%
math.factorial(6)

# %% [markdown]
# # Hadith
# "The excess of ilm is better than the excess of ibadah , and the best of your religion is the "wara" (self retrain)

# %%
from math import sqrt
sqrt(7)

# %%
# using From to import
from math import pi,  sqrt
pi


# %%
from math import *
# function are define in already , not take this function name (as varaiable ) during coding

# %% [markdown]
# # Function in Python

# %%
# A FUNCTION IS ABLOCK OF CODE THAT START WITH THE DEF KEYWORD 
def add(a,b):
    return a+b


# %%
add(a=2 ,b=3)

# %%
def mpty_function():
    pass


# %%
total = add(a=4,b=5)
print(total)

# %%
# keyword argument
def keyword_function(a=2 ,b=5):
    return a+b

# %%
keyword_function(a=2 ,b=5)

# %%
def mixed_function(a=2,b=5,c=6):
    return a+b+c

# %%
mixed_function(a=2 ,b=5,c=6)

# %% [markdown]
# # Infinite argument and keyword argument using * and **

# %%
def many(*args , **kwargs):
    print(args)
    print(kwargs)

# %%
many = (1,2,3, name:= "tayyaba" , job:= "teaching")
print(many)

# %% [markdown]
# # global scope:
# scope tell us when varaiable  is avaiable to use and where.

# %%
# example of scope and global
def function_a():
   global a
   a= 5
   b= 3
   return(a+b)


def function_b():
    c= 3
    return a+c
    print(function_a())
    print(function_b())    

# %% [markdown]
# # class in python
# - " Teach! make things easy! and do not make things complicated!  (Ameeen)

# %%
x = "alnafi"
dir(x)

# %% [markdown]
# # 

# %%
class Vehicle (object):
  """docstring"""
def _init_ (self):
     """Constructor"""
     pass

# %%
class vehicle(object):
    """docstring"""
def  _init_(self, color,doors, tires) :
    """Constructor""" 
    self.color = color
    self.doors = doors
    self.tires = tires
def brake(self):
    """      
    stop the car
    """  
    return "Braking"
def drive(self):
    """   
    Drive the car
    """      
    return "I'm driving"

# %% [markdown]
# - string  is an object in python
# - python is an object oriented  languages
# - python has many type of data type.like tuple , dictionary and lists.

# %%
# help(my_string.upper)
#help(my_string.lower)
# help(my_string.translcation)
# type(my_string)

# %%
A = False
B = True
print("one" if A else "python" if B else "ciao!" )

# %%




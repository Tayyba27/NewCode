# Data Structure

# %% [markdown]
# "Greetings to the seeker of knowledge"

# %% [markdown]
# # Python objects and Data  Structures
# 
# - mutable object:( can be change)
# 
# list , dict , set , byte array
# - immutable object:(cannot be change)
# 
# int, float , complex, string , tuple , frozen set ,bytes

# %% [markdown]
# # python beta 101
# - Python and Number 01
# - "Indeed ! Acquiring  knowledge is done through learning!"

# %% [markdown]
# - There are two type of number in python 
# 1) integer  (whole number)
# 2) float (decimal)

# %%
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# %% [markdown]
# - Python and Number 02

# %%
# avoid the varaiable name  like "str " , or "int". whose already define as function in python

# %% [markdown]
# # Dynamic and Static Programming Language:
# 
# - A dynamic language (Lisp, Perl, Python, Ruby) is designed to optimize programmer efficiency, so you can implement functionality with less code. 
# 
# - A static language (C, C++, etc) is designed to optimize hardware efficiency, so that the code you write executes as quickly as possible. 

# %% [markdown]
# - Python and String:
# - string are sequence of character
# - string slicing and  indexing
# - character  [i     s       l       a  m]
# - index    [ 0      1        2     3      4]
# - slicing allows us to grab a subsexction of multiple character

# %%
"I'm going to teach python"     

# %% [markdown]
# # slicing strings:
# 

# %%
mystring = "islam"

# %%
mystring[2]

# %%
mystring[-1]

# %%
mystring[3]

# %%
mystrings = "muhammad fiasal"

# %%
mystrings[::3]

# %%
mystrings[::4]

# %%
mystrings[1:]

# %%
a = "Salam"

# %%
a = a +" means peace!"
print(a)

# %%
letter = " a"
letter *4
# * symbol for multiple as exponent

# %%
5 +5
# adding

# %%
"5" +"5"    
# concatination

# %%
x = " Al Nafi"
x

# %%
x.upper()

# %%
x.lower()

# %%
x.split()
#  function of split "organize  given variable as a list "

# %% [markdown]
# # string formatting method
# 
# - string interpolation:
# 
#  is a process substituting values of variables into  placeholders in a string.
# 
#  1) Format ()
#  2) f-strings()

# %%
print("Al Nafi is a")

# %%
print("Al Nafi is a {}" .format("good institute!"))

# %%
result = 100/334
result

# %%
print("the reslt was {}" .format(result))

# %%
print("the reslt was {: 1.3f}" .format(result))

# %%
name = "Tayyaba"
name

# %%
print(f'Salam, my name is {name}')

# %% [markdown]
# # list in python

# %%
my_list = [1,2,3]
my_list

# %%
my_list.sort()

# %%
len(my_list)

# %%
my_list[2]

# %%
my_list[1:]

# %%
my_list[:1]

# %% [markdown]
# # list and Dictionary

# %% [markdown]
# - dictionary is a collection whh is unordered  , changeable and indexed 
# - written in curly bracket

# %%
dict_1 = {"key1":"value1" , "key2":"value2"}
dict_1

# %%
dict_1["key1"]

# %%
prices_lookup = {'pence' : 100 , "jpurnel" :40 , "box": 30}
prices_lookup

# %% [markdown]
# # set in python
# - sets are unordered and unindexed collection of unique element.

# %%
myset = { 1,2,3,4,5,7}
myset

# %%
myset.add(6)
myset.add(6)

# %%
my_list = [ 1,1,1,1,2,2,2,2,3,3,3,3,4,4,5]
my_list

# %%
 # tuple 
t = (1, 3,5,7,9)
print(t)

# %%
mylist = [1,2,3]
mylist

# %%
type(mylist)

# %%
len(t)

# %%
t[1]

# %%
t[3]

# %%
t = ('alnafi' , 'python' , 'cissp')
t

# %%
t.count('alnafi')

# %%
t.count('cissp')

# %% [markdown]
# # Boolean in python
# -  two constant object which can either Ture or False
# - logic is key to control
# 
# 
# 
# # Logical Boolean Operators
# -  Logic AND -----------  if both the operands are ture then condition are ture
# -  Logic OR   ----------  If any of the two operands are non-zero then condition becomes ture 
# -  Logic NOT ----------- used to reverse the logical state of its operand

# %%
1<5 and 7<6

# %%
5<9 or 4<9

# %%
type(True)

# %% [markdown]
# # Input and Output in Python
# - 

# %%
#%%writefile myfile.txt
#Aslam o Alikum wrwb
#This Al Nafi python beta lecture
#We are going to learn input and output functions

# %%
myfile = open('myfile.txt')

# %%
myfile.read()

# %%
myfile.seek(0)

# %%
myfile.readline()

# %%
myfile.readline()

# %%
myfile.readline()

myfile.pwd()

# %% [markdown]
# # if , elif and else
# - the key statement is 
# - if 
# - elif
# - else

# %%
tired = False
if tired:
    print("sleep")
else:
    print("get bak to work")    

# %%
tired = True
if tired:
    print("sleep")
else:
    print("get bak to work")

# %%
location = 'Masjid'
if location == 'Restaurant' :
    print('eat at sharfoo restaurant')
elif location == 'bank':
    print('get some money from the atm')   
else:
    print('pray your salah')    

# %%
location = 'bank'
if location == 'Restaurant' :
    print('eat at sharfoo restaurant')
elif location == 'bank':
    print('get some money from the atm')   
else:
    print('pray your salah') 

# %%
location = 'Restaurant'
if location == 'Restaurant' :
    print('eat at sharfoo restaurant')
elif location == 'bank':
    print('get some money from the atm')   
else:
    print('pray your salah') 

# %% [markdown]
# # loop in python
# - a for loop used i

# %%
mylist=  [1,2,3,4,5,6,7,8,9,10]
mylist

# %%
for num in mylist:
    if num % 3==0:
        print(num)
    else:
        print(f'odd number : (num)')    

# %%
list_sum = 0 

for num in mylist:
    list_sum = list_sum +num
    print(list_sum)

# %%
mytuple = (1,2,3,4)

for item in mytuple:
    print(item)

# %%
second_list = [ (1,4), (4,6) ,(6,9)]
second_list

# %%
len(second_list)

# %%
for (a,b) in second_list:
    print(b)

# %%
x = 0

# %%
x = 0

while x<10 :
    print(f'the current value of x is {x}')
    x = x+1

# %% [markdown]
# # classes

# %%
class Dog():
    def __init__(self , bread):
            self.bread = bread

sam = Dog(bread = "lab")  
frank = Dog(bread = "huskie")         

# %%
sam.bread

# %%
frank.bread

# %%
class Dog():
    def __init__(self , bread , name):
            self.bread = bread
            self.name = name

sam = Dog(bread = "lab")  
frank = Dog(bread = "huskie")

# %% [markdown]
# # Python Beta Next Level  Up 1
# - Basic Information
# - Built -in Modules
# - Testing and Debugging
# - Modulle installation and confiration

# %%
# section 1
# Variable , Basic operator 
# python data structure
# loop 
# comprehension
# error handling
# reading and writting files
# functions
# object oriented programming


# %% [markdown]
# # variable  creation
# - Basic Data types 
# - basic built _in functions

# %%
x = " Bismillah"
y = 1
z = True

# %%
print(x,y,z)

# %%
x= y=z = "Bismillah , 56, True"
print(x,y,z)

# %%
a = 56
b= 67
print(a+b)

# %%
summation = "Hello" + "World"
print(summation)

# %% [markdown]
#  - %  modules operator 
#  - * multiply
# - **   power

# %%
type(198)

# %%
len([1,2,3,4,5,6,7])

# %% [markdown]
# # python data structure
# - containers of different shapes and sizes.
# list:
# store collection of data together (int , str , bool)
# 

# %%
my_first_list = [] 
my_second_list = list()
my_list = [1,2,3,4]
my_new_list = [value for value in range(10)]
my_new_list


# %%
my_new_list[1:]

# %%
my_new_list.append(10)
my_new_list

# %% [markdown]
# # Dictionr creation 
# - store key- value pair together
# {}

# %%
my_first_dict = {}
my_second_dict = ()


# %%
dict_ = {keys : value for keys , value in [['apple ', 12], ['banana ', 14], ['orange', 17]]}
dict_

# %%
dict_1 = {'apple ': 12, 'banana ': 14, 'orange': 17}
dict_1

# %%
dict_1

# %%
dict_1['peach'] = 54

# %%
dict_1

# %%
dict_1['peach']

# %% [markdown]
# # Tuple creation 
# - store a sequence , it is similar to list
# - 

# %%
my_tup = ('jeo' , 'True' , 78 , 9 )
my_tup

# %%
my_tup[0]

# %% [markdown]
# #  control flow  statement:
# - its ability to execute based on fulfillment of a condition.
# - the if , elif and else statement is know as control flow statement
# - all logical operators

# %%
number = 0
if  number %2 ==0 and number != 0:
    print(' this ia an even number')
elif number %2 != 0:
    print('this ia an odd number')  
else:
    print('this ia an zero')     

# %% [markdown]
# # loops
# -   a much easier and convenient alternative.

# %%
name = [ 'ahmad' , 'ali', 'kashif']
name

# %%
for i in range(len(name)):
    name[i] = 'Mr .' +name[i]

# %%
name

# %%
my_fruit = [ 'apple ', 'banana' , 'orange']
for fruit in my_fruit:
    print('I love ' , fruit)

# %% [markdown]
# # functions
# - python allow to re-use code snippets by turnning them into method or function.

# %%
def is_even(number):
    if number %2 ==  0 :
        return True
    else:
        return False    

# %%
print(is_even(5))

# %%
print(is_even(8))

# %%
data = []
f = open('C:\\Users\\3\\Desktop\\Test.txt' 'r')
for row in f:
    r = row.strip('\n')
    data.append(r)

f.close()    

# %%
f = open('C:\\Users\\3\\Desktop\\Test.txt')
print(f)

# %% [markdown]
#  # class
#  - specual method  _ init_

# %%
# create class
class Bike:
    name = ""
    gear = 0

# create objects of class
bike1 = Bike()

# %%
Fruit = [ 'berry']

# %%
#class Citrus(Fruit):
    #def __init__(self , name , nutrirents):
        #super().__init__( name , nutrirents)
        #self.type = ' Citrus'
        #self.characteristic = ' puply and juicy'

    #def get_type(self):
        #return self.type    

# %%
class Dog():
    def __init__(self , bread):
        self.bread = bread
        
sam = Dog(bread = 'lab')
frank = Dog(bread = 'huskie')        

# %%
sam.bread

# %%
frank.bread

# %%
class Dog():

    species = 'mammal'
    

    def __init__(self , bread , name):
           self.bread = bread
           self.name = name



# %%
sam = Dog('lab' ,'Sam')
sam.name
frank = Dog('huskie' ,'Frank')
frank.name

# %%
# string ... method
name = "tayyaba"
name.upper()

# %%
class Circle():
    pi = 3.1415

    def __init__(self , radius = 1):
         self.radius = radius
        

    def area(self):
         return self.radius*self.radius*Circle.pi    
    
    def  setradius(self , radius):
         self.radius = radius

# %%
c1 = Circle()

# %%
c1 = Circle(2)
print(c1.area())

# %%
c1.setradius(5)
print(c1.area())

# %%
class Animal():
    def __init__(self):
        print('Animal Created')
        

    def whoamI(self):
        print(Animal)  

    def eat(self):
        print('Eating')   

# %%
d1= Animal()

# %%
class Dog():
    def __init__(self):
        print('Dog is created')

    def whoamI(self):
        print('Dog')

    def bark(self):
        print('Woof!')    


# %%
d = Dog()

# %%
d.whoamI()

# %%
d1.eat()

# %%
d.bark()

# %%
class Book():
    def __init__(self, title , author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
         return "Title: {} , Author:{}, Pages:{} ".format(self.title, self.author , self.pages)


# %%
book = Book('Python ', 'Tayyaba' , 100)
print(book)

# %% [markdown]
# # Built -in Modules
# - Dates
# - OS model
# - Introspection
# - Sqlite model
# - csv module
# - sub process module
# - Request models

# %%
# Date (datetime)
# python has built in module that allow easy interaction with date and time.
# .. handly different from integer and float.as_integer_ratio. if your data contain dates, you sould ideally use the built - in module, to handle a date while readng the data files
from datetime import datetime

# %%
my_dt = datetime.now()

# %%
year = my_dt.strftime("%y")
month = my_dt.strftime("%m")
day = my_dt.strftime("%d")
print("day :" , month)

# %%
time = my_dt.strftime("%H:%M:%S")
print(time)

# %%
my_dt = datetime.now()

# %%
date_string = "21 June , 2018"
type(date_string)

# %%
date_object = datetime.strptime(date_string , "%d %B , %Y")
type(date_object)

# %% [markdown]
# # OS Module (operating system )
# the  built-in os  modules  help interact  with the operating system through python.
# you can create , access , verify and manipulate file paths using the os module, you check and set your working directory
# 

# %%
# Return the path for current directory
import os
os.getcwd()

# %%
# specific path
os.listdir()

# %%
# change current directory to "path"
os.chdir("c:\\")

# %% [markdown]
#  - os.path.exists(path)    
# ( check if provide path exist)
# 
# - os.path.join(args*)
# ( join folder names together to form a valid path)
# 
# - os.path.split(path)
# ( splits directory into folder names ,path must be in a valid directiry format)
# 
# - os.path.isfile(file_name)
# ( checks wether the file name points to an actual file in the directory)
# 
# - os.path.isdir(path)
# ( checks wether path to an actual file directory)
# 
# - os.mkdir(path)
# (  a folder in the specified directory)
# 
# 

# %% [markdown]
# # Introspection Module
# in python help s determine type of object, its attributes and method at runtime.
# it is useful to understanding the structure of the data and at times  method tied to an object.
# allow a user  to perform these action on any python object or variable.
# 
# 
# 1)- Basic Method
# type() .
#  dir() . 
# unique id()
# 

# %%
my_var = "This is a variable"
my_num = 453.324
my_greeter = "Greeter"
class Greeter:
    def _init_(self , _name):
        self.name= _name
    def say_hello(self):
        print('Hello {}!' .format(self.name))
    def say_goodbye(self):
        print('Goodbye {}!' .format(self.name))
        my_greeter = Greeter('jhon')
        print(my_greeter)  

print('Get id , type and avaiable methods and attribute for Greeter class')
print(id(my_greeter))
print(type(my_greeter))
print(dir(my_greeter))

print('Get id , type and avaiable methods for a variable conyaining numeric value')
print(id(my_num))
print(type(my_num))
print(dir(my_num))

print('\ncheck id , type and method for variable containing string')
print(id(my_var))
print(type(my_var))
print(dir(my_var))



# %%
print('Get id , type and avaiable methods and attribute for Greeter class')
print('\ncheck id , type and method for variable containing string')
print(id(my_var))
print(type(my_var))
print(dir(my_var))

# %%
print('Get id , type and avaiable methods for a variable conyaining numeric value')
print(id(my_num))
print(type(my_num))
print(dir(my_num))

# %%
print('Get id , type and avaiable methods and attribute for Greeter class')
print(id(my_greeter))
print(type(my_greeter))
print(dir(my_greeter))
# not working

# %%
import inspect
import os
testvar = 'Hello'

class Greeter:
    def _init_(self , _name):
        self.name= _name
    def say_hello(self):
        print('Hello {}!' .format(self.name))
    def say_goodbye(self):
        print('Goodbye {}!' .format(self.name))
        my_greeter = Greeter('jhon')


    # lambda function (for temporary used)
    exp = lambda x: x*x

# normal python user defined function
def show_name_age(first_name:str , last_name :str, age:int):
    print ('{} {} is {} years old ' .format(first_name , last_name , age))






# %%
import os 
testvar = 'Hello'

exp = lambda x, y :x*y


# %%
inspect.ismodule(os)

# %%
inspect.isfunction(exp)

# %%
inspect.isfunction(my_greeter.say_goodbye)
# false

# %%
inspect.ismethod(my_greeter.say_goodbye)
# ture

# %% [markdown]
# # Sqlite Model:
# 

# %%
import sqlite3
from sqlite3 import Error

# %%
def create_table_in_db(conn, create_table_sql):
    """     Create a table from the create_table_sql statement
    :param conn : Connection object
    :param: create_table_sql:  a CREATE TABLE statement 
    : return:
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e :
        print(e)    
    

# %%
import sqlite3
from sqlite3 import Error

# %%
def create_connection(db_file):
       """   Create a database Connection to the Sqlite darabase specified by db_file 
    :param db_file : database file
    : return: Connection object or None
    """ 
       
       conn  = None
       try:
          conn = sqlite3.connect(db_file) 
          print("The Sqlite connection is connected")  
          return conn
       except Error as e :
              print(e)




# %%
def close_connection(conn):
      """   Create a database Connection to the Sqlite darabase specified by db_file 
    :param conn : db_connection object
    : return: 
    """
      if(conn):
         conn.close()
      print("The sqlite connection is closed") 

# %%
def create_table_in_db( conn , create_table_sql):
          """     Create a table from the create_table_sql statement
          :param conn : Connection object
          :param: create_table_sql:  a CREATE TABLE statement 
          : return:
          """
          
          try:
              c = conn.cursor()
              c.execute(create_table_sql)
          except Error as e:
            print(e)

# %%
def create_table():
    database = r"D:\Downloads\database.db"
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS STUDENTS(
    id interger  PRIMARY KEY,
    name  text NOT NULL,
    gpa integer,
    admission_date text
    );
    """

    conn = create_connection(database)

    if conn is not None:
        create_table_in_db(conn , sql_create_projects_table)
    else:
        print("Error! can not create database connection")  
    close_connection(conn)  

# %%
create_table()

# %%
# add student code
def add_student(conn, student) :
    """ Create a new student entry into the student table 
    :param conn:
    :param student:
    :return: student id

    """


    sql = '''INSERT INTO STUDENT(name , gpa ,admission_date)
                VALUE(?,?,?)  '''
    cur = conn.cursor()
    cur.execute(sql, student)

    return cur.lastrowid

# %%
database = r" C:\\Desktop\Study.pydir\database.db"

conn = create_connection(database)
with conn:

    std = ['Ahmed Akbar' , 3.7 , '2019-10-30']
    std_id = add_student(conn , std)

print("The student id is : " , std_id)

close_connection(conn)   

# %%
# read table  
database =r" C:\\Desktop\Study.py\database.db" 
conn = create_connection(database)

try:
    cursor = conn.cursor()

    table_name = "STUDENT"
    sql_string= "SELECT * from " + table_name
    sqlite_select_query = sql_string
except:
    print("Total row are :" , len)




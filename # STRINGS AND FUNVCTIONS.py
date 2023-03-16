#  String and Function
#  String Slicing 
# is used a lot in real life . within machine learning , deep learning , data wrangling , AI , website  and game.

my_string = "My Country Pakistan"
my_string [0:5]
print(my_string[0: 20])

# string substitution
var = "cookies"
newstring = "I like  %s " % var
newstring

var = "cookies"
anotherstring = "I like  %s and %s  " % ("python" , var)
anotherstring

my_string = " %i + %i = %i " % (1,2,3)  # integer
my_string

# %%
# float
float_string = "%.5f" % (1.3456)       # 5f means the five digit after point.
float_string

# %%
print("%(x)i +%(y)i = %(z)i"  %{"x":1 , "y":2 ,"z":3})
"python  is as simple as {0} ,{1} , {2} ".format("a" ,"b" ,"c")

# %%
# Nested list
my_list =[1,2,3]
my_list2 = ["a", "b","c"]
my_list3 = ["a" ,1 , "Python" , 6]
my_nested_list = [my_list, my_list2 ,my_list3]
print(my_nested_list)

# list extend method
combo_list =[]
one_list = [4,5]
combo_list.extend(one_list)
combo_list

my_list =[1,2,3]
my_list2 = ["a", "b","c"]
combo_list = my_list+my_list2
combo_list

# sorting out a list 
alpha_list =[34,76,56,54,43,23]
sorted_list = alpha_list.sort()
print(sorted_list)

# %%
# dictonary
dict = {"name" : "Sharfoo" , "addres" : "123 Gulshan"}
dict["addres"]

# %%
dict = {"name" : "Sharfoo" , "addres" : "123 Gulshan"}   # important of "In"
dict.keys()

# %%
dict = {"name" : "Sharfoo" , "addres" : "123 Gulshan"}
dict.values()

dict = {"name" : "Sharfoo" , "addres" : "123 Gulshan"}
#"name" in dict     for Ture
"state" in dict

#Function
if 2>1:
    print("This is a Ture statement")

var1 = 3
var2 = 5
if var1 > var2:
    print("This is also True")
else:
    print("This is a False")    

    
value = 45
if value <10:
    print("That's a great deal!")
elif 10<= value<=20:
    print("I'd still pay that..")    
else:
    print("Wow! That's too much..")   

# %%
# boolean      Ture or False
# or ,,,and   ,,, not


x =  13
y =  10
if x<10 or y> 15 :
    print("This is statement was Ture")


my_list = [1,2,3,4]
x = 10 
y = 11
if x not in my_list and y != 10:
    print("This is Ture! ")
else:
    print("This is False !")    

x = 8
if x != 11:
    print("This is Ture !")

#if empty_list == []:              This code is not running
    #print("it's an empty list")
#if empty_tuple:
    #print("It's an empty tuple")
#if not empty_string:
    #print("This is an empty string")
#if not nothing:
    #print("Then it's nothing !")    


# %%
if 2>8:
    print("This is a Ture Statement")

print("This ia a  backslash \\")

dict = {"one":1,"two":2, "three":3}

for key in dict:
    print(key)       


for number in range(10):
  if number %2==0:
    print(number)

a_dict = {1:"one",2:"two",3:"three"}
keys = a_dict.keys()
sorted(keys)
for key in keys:
    print(key)

    
x =[i for i in range(5)]
print(x)

# Nested list comprehension
list =[[1,2,3],[4,5,6],[7,8,9]]
[num for elem in list for num in elem]

# %%
# dictionary comprehension
print({i:str(i)  for i in range(5)})


my_dict = {1:'dog',2:"cat",3:"horse"}
print({value:key for key, value in my_dict.items()})

# set coprehension
my_list = [1,2,2,3,3,4,5,6,7,8]
my_set = set(my_list)
my_set

my_list = [1,2,3,4,5]
for i in my_list :
 if i ==3:
    print("items found!")
    break
else:
    print(i)
    print("items not found!")

# # EXCEPTIONS HANDLING IN PYTHON
# # Common python Error
#  Exception ,
#  AttributeError,
#  IOError ,
#  ImportError ,
#  IndexError ,
#  KeyError ,
#  Keyboardinterrupt ,
#  NameError ,
#  OSError ,
#  SyntaxError ,
#  TypeError ,
#  ValueError ,
#  ZeroDivisionError .
# 


#1/0
# solution (  try or except )

try:
    1/0
except ZeroDivisionError:
    print("You cannot divide by zero!")    

# finally exception

my_dict = {"A":1 , "b":2 ,"c":3}
try:
    value =my_dict["d"]
except KeyError:
    print("A KeyError occured")
finally:
     print("The finally statement has executed")       

my_dict = {"a":1 , "b":2 ,"c":3}
try:
    value =my_dict["a"]
except KeyError:
    print("A KeyError occured")
else:
    print("No error occured")    

my_dict = {"a":1 , "b":2 ,"c":3}
try:
    value =my_dict["a"]
except KeyError:
    print("A KeyError occured")
else:
    print("No error occured") 
finally:
     print("the finally statment ran!")    

# # Quiz 01:
    1) if s:= 'The propitious':
    print(s[3:])


2) if s := "hello":
    print(s[1])

3) # Are string immutable "
# Yes

# # python comprehension
# the python language has acouple of methods for creating list and dictionary is called python comprehension

x= [i for i in range(5)]
print(x)

# # strip the list
myStrings = [s.strip()for s in my_string]
vec = [[1,2,3],[4,5,6],[7,8,9]]              
# later give the best exapmle of strip the list

# # list comprehension

mylist = [ tayyaba for tayyaba in "alnafi"]
mylist



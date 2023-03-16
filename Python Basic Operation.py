
## Basic Operation   
#     +     addition
#     -     subtraction
#     *     multiplication
#     /     forward selation  division
# 


56890+43218

7865*654

125//5


 # The order of operation
# 5+30*20 = 605
# mulitplication & DIVISION are first use the addition and substraction use. 
# parentheses can change the order of operation

# # variable
# variable in programming  means a place to store information  such as number , text , list of number.

# string 
df= "first caliph"
df

# backslash \ "yes i know i have quotes inside my string  and  want you to ignor them untill you see the end quote"
single_quote_str = 'He said ,"Aren\'t can\'t shouldn\'t wouldn\'t "' 
print(single_quote_str)


# Embedding value in string ( inserting value)
myscore = 1000
message = 'I score %s poiunts '
print(message % myscore)

nums = 'What did the number %s say to the number %s ? Nice belt'
print(nums %(0,8))

# Multiplying string 
print(10 * "b")

spaces = '' * 25
print( '%s 12 DHA Phase 5' % spaces)
print('%s Clifton ' % spaces)
print('%s West Snorng' % spaces)
print()
print()
print('Dear Sir,')
print()
print('I wish to report that tiles are missing from the')
print('outside toilet roof.')
print('I think  it was bad wind the other night that blew them away.')
print()
print('Regards')
print('Sharfoo')




spaces = '' * 25
print( '%s The Principal' % spaces)
print('%s A.b.C. ' % spaces)
print('%s Mustafa Abad' % spaces)
print()
print()
print('Dear Sir,')
print()
print('I beg to say that , I am ill. So I cannot come ')
print('to school .')
print('Kindly grant me leave for one day .')
print()
print('Your obediently,')
print('Regards,')
print('Tayyaba Anwer')





print(1000* "KARACHI")

sharfoo_list = 'vegetable , fruit , samosa , tea'
print(sharfoo_list)

# List can store all sort of terms 
some_number = [1,2,5,10,20]
number_and_strings = ['Why','was', 6 , 'afraid', 'of' ,7, 'beacuse' , 7,8,9]
print (number_and_strings)


# list within a list
numbers = [1,2,3,4]
strings = ['I','kicked' , 'my' , 'toe', 'and','it' , 'is', 'sore']
mylist = [numbers , strings]
print(mylist)

wizard_list = ['spider legs' , 'toe of frog' , 'eye of newt' ,' bat wing' , 'slug butter', 'snake dandruff']
print(wizard_list)
wizard_list = ['spider legs' , 'toe of frog' , 'eye of newt' ,' bat wing' , 'slug butter', 'snake dandruff']
wizard_list. append('bear burp')
print(wizard_list)


wizard_list = ['spider legs' , 'toe of frog' , 'eye of newt' ,' bat wing' , 'slug butter', 'snake dandruff']
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)


# Sum  & Product of two list are possible , but division and subtraction of to list are not possible
list1 =[1,2,3,4]
list2 = ['I', 'ate', 'chocolate' , 'i' , 'want' , 'more']
list3 = list1+list2
print(list3)

list4 = [5,6]
print(list4 *6)


# Tuple
# a tuple is like a list that uses prentheses like as ,
fibs = (0,1,1,2,3)
# in tuple can never change the values in list.

# IF statement
age = 21
if age > 20:
    print('you are too old')

age = 21
if age > 20:
    print('you are too old')
    print('Why are you here?
          
# # condition in python 
# == equal to 
# <  greater than
# >  less than 
# ! = is not equal to
# 


print(" Want to hear  a dirty joke?")
age =12
if age == 12:
    print("a pig fell in the mud")
else:
     print("Shh . It's a secret")   


age = 10 
if age == 10:
    print('What do you call an unhappy cranberry?')
    print("A blueberry")
elif age == 11:
    print("What did thr green grape say to the blur grape?")
    print("Breathe ! Breathe !")
elif age == 12:
    print("What did 0 say to 8 ?")
    print("Hi guys!")
elif age ==13:
    print("Why wasn't 10 afraid  of 7")
    print("Because raher than eating 9, 7 8 pi .")
else:
    print("Huh?")


# difference betweeen string and number
age = 10  # (number)
if age == 10:
    print("What's the best way to speak to a monster?")
    print("From as f away as possible")

age = '10'  # (string)
if age == 10:
    print("What's the best way to speak to a monster?")
    print("From as f away as possible")

#  this way the answer or reasult are not showed ......for string use integer

age = '10'  # (string)
Converted_age = int(age)
if Converted_age == 10:
    print("What's the best way to speak to a monster?")
    print("From as f away as possible")


# # loop
# # for , while , range
          
for x in range (0,5):
    print('Salam')

# using range and list together
print(list(range(10,20)))



#printing in twice
hugehairypants= ['huge'  'hairy' , 'pants']
for i in hugehairypants:
    print(i)
    print(i)

# # for :
# A for loop is a loop of specific length
# # while:
# while loop  is a loop that used when you don't know ahead of time when it needs to stop looping 

x = 45
y= 80
while x< 50 and y<100:
    x= x+1
    y= y+1
    print(x,y)

# code and function modules
list(range(0,8))

import time 
print(time.asctime)

#testfun('marry')

def testfun(myname):
    print("hello %s" % myname)

#creating variable
firstname = 'mohammad'
lastname = 'omar'
#testfun(firstname, lastname)
print(firstname, lastname)


# using return
def variable_test ():
    first_variable = 10
    second_variable = 20
    return first_variable*second_variable
    print(variable_test())
          

# A Module is a python object with arbitrarily
# a module can be defin function, classes  and variable
# also include runnable code

import time
print(time.asctime())
          
# objects and classes

# python build_ in _function

# python abs
# the syntax abs()     parameter 
#abs(num)     num--- integer , floating , complex number

# # bool    (True or False)
# 
# the following  values are consider 
# - zero of any numerical type
# - empty sequence   ()[]
# - empty mapping{}



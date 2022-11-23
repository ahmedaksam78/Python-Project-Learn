




print (5*' احمد اكسم\n')
print (2*'32\n')
#This is a comment.
"""
This is a comment
written in
more than just one line
"""

x = 5
y = "Hello, World!"
#This is to print y 
print(x)
print(y)

x = str(3)    # x will be '3'
y = int(45)    # y will be 3
z = float(3.86)  # z will be 3.0

print(type(x))
print(type(y))
print("test",end="// ")
print("test2")


print("test1","test2","test2",sep=" ,,,")
print(x,y)

# name="ahmed" age=12  coutry="EG"
name, age,country="ahmed",12,"EG"
print (name,age,country)
name= age=country
print (name,age,country)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
######
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

#   methods  
text="ahmed aksam"
text2="AHMED AKSAM"
txt="AhMeD AkSaM"
print(len(text)) # to get lenght of the string
print( text.capitalize() ) # to covert first letter on string to capital
print( text2.casefold() )  # to convert the string to lowercase
print( text.upper() )  # to convert the string to uppercase
print( text2.lower() )  # to convert the string to lowercase
print( txt.swapcase() )  # to convert the string to swap case
print( text.title() )  # to convert the first char from each word to capital

print( text.count("a") )  # to count some substring
print( text.count("am") ) # to count some substring
print( text.count("amh") ) # to count some substring

print( text.endswith("am") ) # to check if string end with some substring or not
print( text.startswith("Am") ) # to check if string Srart with some substring or not

print( text.find("m") ) # to find some substring return index if not found it retun -1
print( text.rfind("m") ) # to find some substring return index if not found it retun -1
print( text.find("r") ) # to find some substring return index if not found it retun -1

print( text.index("m") ) # to find some substring return index if not found it retun error
#print( text.index("r") ) # to find some substring return index if not found it retun error
print( "a" in text ) # to find some substring true or false

print( text.rindex("a") ) # to find some substring return index if not found it retun error
print( text.rindex("a") ) # to find some substring return index if not found it retun error

text3="    samy Ramy    "

print( text3.strip() ) # to remove spaces from string left and right
print( text3.lstrip() ) # to remove spaces from string left 
print( text3.rstrip() ) # to remove spaces from string right

print(text.replace('aksam','abdelhameed')) # to replace subString with another


text12='Ahmed Aksam Abdelhameed2222'
text13='ahmedaksamabdelhameed'
text14='655656765.656576576'
text15='655656765'

print(text12.isalnum())# check if string is number and alphapetic  or not
print(text14.isalnum())# check if string is number and alphapetic  or not
print(text15.isalnum())# check if string is number and alphapetic  or not

print(text13.isalpha())# check if string is alphapetic or not
print(text14.isalpha())# check if string is alphapetic or not

print(text14.isdigit())# check if string is digits or not 
print(text15.isdigit())# check if string is digits or not

print(text14.isdecimal())# check if string is decimal or not 
print(text15.isdecimal())# check if string is decimal or not 

print(text14.isidentifier())# check if string is identifier to name a variable or not 
print(text13.isidentifier())# check if string is identifier to name a variable or not 

print(text13.islower())# check if string is  in lower case or not 
print(text12.islower())# check if string is  in lower case or not

print(text2.isupper())# check if string is in upper case or not 
print(text12.isupper())# check if string is in upper case or not  

print(text13.istitle())# check if string is title or not 
print(text12.istitle())# check if string is title or not  
a = "Hello, World!"
print(a.split(",")) 





'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List        : is a collection which is ordered and changeable. Allows duplicate members.
Tuple       : is a collection which is ordered and unchangeable. Allows duplicate members.
Set         : is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary  : is a collection which is ordered** and changeable. No duplicate members.
'''

x1 = ["apple", "banana", "cherry"]# list
x2 = ("apple", "banana", "cherry")#tuple
x3 = {"apple", "banana", "cherry"}#set
x4 = dict(name="John", age=36) #dict

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
    
    
b = "Hello, World!"
print(b[2:5])
print(b[-5:-2])
print(b[2:])
print(b[:5])

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

x = 200
print(isinstance(x, int))
"""
list MEthods
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# for remove an item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
thislist.pop()
print(thislist)
# For remove the list

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loops in list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# get items that have char a
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
        print(newlist)

#List objects have a sort() method that will sort the list alphanumerically, ascending, 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#List objects have a sort() method that will sort the list alphanumerically, ascending, 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

###############
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#################
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) 
##########
#copy list to another
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
##
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
##
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

##
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

'''
tupple methods
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''
#################################
#tuple
#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#Assign the rest of the values as a list called "red": *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
##########################################

"""
sets MEthods
add()	                        Adds an element to the set
clear()                      	Removes all the elements from the set
copy()                        	Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()         	Removes the items in this set that are also included in another, specified set
discard()                   	Remove the specified item
intersection()	                Returns a set, that is the intersection of two other sets
intersection_update()          	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()                          	Removes an element from the set
remove()	                    Removes the specified element
symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others
"""
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
###
#Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)



#To add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3,"a"}
set3 = set1.union(set2)
print(set3)
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3,"a"}
set1.update(set2)
print(set1)

#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


##########
'''
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

####
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)

###
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
print(x)

x = thisdict.keys()
y = thisdict.values()
print(x)
print(y)
####
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
####
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
##
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

####
#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
###
#Another way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
###
for x in thisdict:
  print( x ,thisdict[x])
###
print("#########")
for x, y in thisdict.items():
  print(x, y)
#######
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
###################
print("A") if a > b else print("B")
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
#
for x in range(6):
    print(x)
    
############
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
        
#############################
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
################################
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

################
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
###################
x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#####################
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

###############################
##iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

####################
from dbm import _Database
import Person as mx
p2= mx.Student(" ahme aksam" ,"aksam",2113)
p2.welcome()

from Person import Person 
p2= Person(" ahme aksam" ,"aksam")
p2.printname()

import platform

x = platform.machine()
print(x)

###################
'''
%a	Weekday, short version	                                        Wed	
%A	Weekday, full version	                                        Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	                        3	
%d	Day of month 01-31	                                            31	
%b	Month name, short version	                                    Dec	
%B	Month name, full version	                                    December	
%m	Month as a number 01-12	                                        12	
%y	Year, short version, without century	                        18	
%Y	Year, full version                                          	2018	
%H	Hour 00-23	                                                    17	
%I	Hour 00-12	                                                    05	
%p	AM/PM	                                                        PM	
%M	Minute 00-59	                                                41	
%S	Second 00-59	                                                08	
%f	Microsecond 000000-999999                                   	548513	
%z	UTC offset	                                                    +0100	
%Z	Timezone	                                                    CST	
%j	Day number of year 001-366	                                    365	
%U	Week number of year, Sunday as the first day of week, 00-53 	52	
%W	Week number of year, Monday as the first day of week, 00-53	    52	
%c	Local version of date and time	Mon Dec 31 17:41:00             2018	
%C	Century	                                                        20	
%x	Local version of date	                                        12/31/18	
%X	Local version of time                                          	17:41:00	
%%	A % character	                                                %	
%G	ISO 8601 year	                                                2018	
%u	ISO 8601 weekday                                                (1-7)	1	
%V	ISO 8601 weeknumber                                             (01-53)	01	

'''
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
##################################
#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#############
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
#####################
'''
Function	Description
findall 	Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split    	Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
'''
'''

Character	Description	                                                                    Example	
[]      	A set of characters	                                                            "[a-m]"	
\	        Signals a special sequence (can also be used to escape special characters)	    "\d"	
.	        Any character (except newline character)	                                    "he..o"	
^	        Starts with	                                                                    "^hello"	
$	        Ends with	                                                                    "planet$"	
*	        Zero or more occurrences	                                                    "he.*o"	
+	        One or more occurrences                                                     	"he.+o"	
?	        Zero or one occurrences	                                                        "he.?o"	
{}	        Exactly the specified number of occurrences                                 	"he.{2}o"	
|	        Either or	                                                                    "falls|stays"	
()	        Capture and group	 	 

'''

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

######
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

#######
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
######
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
#####
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())

#####################################
#The try block will raise an error when trying to write to a read-only file:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  
###########################
#how to take an input from inputfiled
# username = input("Enter username:")
# print("Username is: " + username)
###############
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
txt = "The price is {:.2f} dollars"
print(txt.format(price))


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
####
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
###
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

###
'''
File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:




"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''
# f = open("demofile.txt", "r")
# print(f.read())
# print(f.read(10))
# print(f.readline())
# print(f.readline())

# #######
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# #f = open("demofile2.txt", "r")
# print(f.read())

# ####
# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the appending:
# #f = open("demofile3.txt", "r")
# print(f.read())


# #######
# #f = open("myfile.txt", "x")
# f = open("myfile.txt", "w")

# #remove file that exist in folder
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
#################

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(np.__version__)
print(type(arr))

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
####
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
####
arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])
#####
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])


'''
We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[1:5:2])

'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

'''

arr = np.array([1, 2, 3, 4])

print(arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
#Make a copy, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#Make a view, change the view, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
###########
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)
##############
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

#Iterate through the following 3-D array:

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

for x in np.nditer(arr):
  print(x)

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
  
  
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
  
#Enumerate on following 1D arrays elements:
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

#We pass a sequence of arrays that we want to join to the concatenate() function
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

#Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
#Stacking Along Columns
#NumPy provides a helper function: vstack()  to stack along columns.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
#Stacking Along Height (depth)
#NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

#################
#search
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)

#######################

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)
######################################

import mysql.connector as mysql



mydb = mysql.connect(
  host="localhost",
  user="root",
  password="Ahmed3218@",
  port="50000"
  
)

print(mydb)
#If this page is executed with no error, you have successfully created a table named "customers".

#Add coments and Print Learning Python
print("Learning Python")

"""
add python script to add multi line comments and
print values of four variables each in a new line
"""
a=2
b=3
c=4
d=5
print(a,b,c,d, sep='\n')

# python script to print types of variables, Create 5 variables each of them containing different types of data. 
a=46
b=True
c="MySirG"
d=4.65
e=2+3j
print(type(a),type(b),type(c),type(d),type(e))

#python script to print the id of two variables containing the same integer values.
a=4
b=4
print(id(a),id(b))

"""
Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable
"""
a=56
b="Hello"
c=False
d=5.6
e=5+6j
print("Unique Id:",id(a),"type:",type(a),"Unique Id:",id(b),
"type:",type(b),"Unique Id:",id(c),"type:",type(c),"Unique Id:",
id(d),"type:",type(d),"Unique Id:",id(e),"type:",type(e), sep='\n')

#python script to print all the keywords
from datetime import datetime
import keyword
from pdb import pm
from time import strftime
from xmlrpc.client import DateTime, _datetime
print(keyword.kwlist)

#Python shell use help() function and display the list of keywords
import keyword
help(keywords)

"""Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py"""
import A1
print(A1.a)

#Name the keywords, used as data in the Python script
import keyword
print(keyword.kwlist[0:3])

#Write a python script to display the current date and time. First create variables to
#store date and time, then display date and time in proper format.
import datetime

x = datetime.datetime(2022,8,13,21,00,00)

print(x.strftime("%d-%m-%Y %I:%M:%S %p"))







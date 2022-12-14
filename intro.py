#  A 'first steps in python' course, made by GIANT Room Innovator MDN (@markdenardo) 2022  

#  Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.

#  https://en.wikipedia.org/wiki/Python_(programming_language)

print("Hello Humans, can't wait to code w y'all.")

#  print() function works like a printer. Put the data, or argument within the parenthese and it will print when you compile your python file:

# try using the print() function in a compiler https://www.programiz.com/python-programming/online-compiler/

x = []           
y = 1          
n = "python"   
b = True       

# prints data
print(x,y,n,b)

# prints data type
print(type(x),type(y),type(n),type(b))

# here are some data types, you may notice that the string data type has quotes
# this is also how we assign a variable and use it in python

sentence = "this is a sentence."
print(sentence)

# getting started, try printing out many things using the print function, maybe create a large billboard of emojis 👑🐉🏆

while True:
  print("🍑⚡️😅⚡️🌋🍕")

#  if we want to perform math in python, we can ask for problems to be solved directly and we'll get answers

1+1

# more interesting things happen when we do variable assignment
#numbers
x=10
y=20

#math
z=(2*x+y)/y

#solution changed to string
value = str(z)

#output
print("the value is " + value)

# we can use python to create list of names

list_of_names = ["Naohmi","Maru","Mark"]
new_name = input('Please enter your name: ')

list_of_names.append(new_name)
output = str(list_of_names)
print("the updated list: " + output)

# when we are using python for data science, a lot of the time we are using APIs 
# An API is an Application Programming Interface https://en.wikipedia.org/wiki/API
  
# See if you can get this code to work, it requires loading two libraries in Python by using import

import requests
import json

r = requests.get("https://api.glitch.com/")
j=r.json()
print(j)


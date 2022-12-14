//  A 'first steps in python' course, made by GIANT Room Innovator MDN (@markdenardo) 2022  

//  Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.

//  https://en.wikipedia.org/wiki/Python_(programming_language)

  print("Hello Humans, can't wait to code w y'all.")
  
  >> Hello Humans, can't wait to code w y'all.

//  print() function works like a printer. Put the data, or argument within the parenthese and it will print when you compile your python file:

// try using the print() function in a compiler https://www.programiz.com/python-programming/online-compiler/

x = 0           //  int
y = 1           //  int, float, complex
n = "python"    //  str
b = True        //  bool

// here are some data types, you may notice that the string data type has quotes
// this is also how we assign a variable and use it in python

sentence = "this is a sentence."
print(sentence)

>> this is a sentence

// getting started, try printing out many things using the print function, maybe create a large billboard of emojis 👑🐉🏆

while True:
  print("🍑⚡️😅⚡️🌋🍕")


//  if we want to perform math in python, we can ask for problems to be solved directly and we'll get answers

1+1
>> 2

// more interesting things happen when we do variable assignment

x=10
y=20

print("the value is " + (2x+y)/y)

// when we are using python for data science, a lot of the time we are using APIs 
// An API is an Application Programming Interface https://en.wikipedia.org/wiki/API
  
// See if you can get this code to work, it requires loading two libraries in Python by using import

import requests
import json

r = requests.get("https://api.glitch.com/")
j=r.json()
print(j)


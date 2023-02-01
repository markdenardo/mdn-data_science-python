# in this lesson we're going over control blocks of code in python

# elif works as an ongoing if then statement 
# if the statement is true, indented code runs 
# test out the elif code by changing the pet type to a type the blocks of code will recognize
pet_type = "snake"

if pet_type == "dog":
  print("You have a dog.")
elif pet_type == "cat":
  print("You have a cat.")
elif pet_type == "fish":
  print("You have a fish")
else:
  print("Not sure!")

#  orOperator
#  or looks for one thing or another to be true
True or True      # Evaluates to True
True or False     # Evaluates to True
False or False    # Evaluates to False
1 < 2 or 3 < 1    # Evaluates to True
3 < 1 or 1 > 6    # Evaluates to False
1 == 1 or 1 < 2   # Evaluates to True

# assignment: make 5 true and 5 false or operator statements

# == equal operator checks if something is the same
# Equal operator

if 'Yes' == 'Yes':
  # evaluates to True
  print('They are equal')

if (2 > 1) == (5 < 10):
  # evaluates to True
  print('Both expressions give the same result')

c = '2'
d = 2

if c == d:
  print('They are equal')
else:
  print('They are not equal')

# Not Equals Operator

if "Yes" != "No":
  # evaluates to True
  print("They are NOT equal")

val1 = 10
val2 = 20

if val1 != val2:
  print("They are NOT equal")

if (10 > 1) != (10 > 1000):
  # True != False
  print("They are NOT equal")

#comparison expression makes comparisons w data
  
a = 2
b = 3
a < b  # evaluates to True
a > b  # evaluates to False
a >= b # evaluates to False
a <= b # evaluates to True
a <= a # evaluates to True

# if Statement checks if something is true

test_value = 100

if test_value > 1:
  # Expression evaluates to True
  print("This code is executed!")

if test_value > 1000:
  # Expression evaluates to False
  print("This code is NOT executed!")

print("Program continues at this point.")

# else Statement says do this when something is not True

test_value = 50

if test_value < 1:
  print("Value is < 1")
else:
  print("Value is >= 1")

test_string = "VALID"

if test_string == "NOT_VALID":
  print("String equals NOT_VALID")
else:
  print("String equals something else!")

# and operator requires both evaluations to be true
True and True     # Evaluates to True
True and False    # Evaluates to False
False and False   # Evaluates to False
1 == 1 and 1 < 2  # Evaluates to True
1 < 2 and 3 < 1   # Evaluates to False
"Yes" and 100     # Evaluates to True

# boolean values check fr True or False
is_true = True
is_false = False

print(type(is_true)) 
# will output: <class 'bool'>

# not operator looks for things to not be a value
not True     # Evaluates to False
not False    # Evaluates to True
1 > 2        # Evaluates to False
not 1 > 2    # Evaluates to True
1 == 1       # Evaluates to True
not 1 == 1   # Evaluates to False

#  syntax error is a way to check your code spelling. it prints out when you have made an error in scripting.
age = 7 + 5 = 4

File "<stdin>", line 1
SyntaxError: can't assign to operator

# This is a udemy course note for learning web development 

## install python 
Python official websiter is https://python.org and we can find and download all the related resources there.
## integers and string in Python
## variables in Python
## Creating variables:
``` python
# Create a variable, my_variable, with the value 5

# Create a variable, x, with the value "Hello, world!"
my_variable =   5
x   =   "Hello, world!"

```

## MEthods : print(),str(),int()


```python
print("I am a student")

x=  5  
I am + x
#this would be a wrong !

# and the write one would be like this :
I am + str(x)

# another examples for int()

y= "I am"
y+10 
# THIS WOULD BE WRONG : 
# RIGHT ONE WOULD BE LIKE THIS :
int(y)+10
```
## methods excersise:   
```python
def exercise():
    # Print the string 'Hello, world!'
    # Make sure that your line is code has space in front of it equal to
    # What these lines have got.
	print('Hello, world!')

# Your code from now onwards must not have any space in front of the lines.

# I have created a variable, num
# Create another variable, str_num, which is num converted to a string
# Psst, you can use the str() method
num = 27
str_num =   str(num)
# I have created a variable, grade
# Create another variable, int_grade, which is grade converted to an integer
grade = '90'
int_grade   =   int(grade)
``` 
## the format() method 
```python
age =5  
I am +str(age)+'years old'
"I am {} years old".format(age)
"I am {} years and {} month old".format(age,7)
"I am {} years old ,are you {} years old ?".format(age=age) 

name = 'Rolf'
# Using the name variable above, create another variable, user_name_phrase
# This should contain the value "Hello, my name is {}". Make sure to use the
# format method!
user_name_phrase    =   "Hello, my name is {}".format(name)

item_name = 'Chair'
item_price = 169.99
# Using the item_name and item_price variables above,
# create another variable, item_details.
# This should contain the value "Item name: {}, price: {}". Make sure to use the
# format method!
item_details    =   "Item name: {}, price: {}".format(item_name,item_price)

friend_name = 'Anne'
friend_age = 30
# Using the friend_name and friend_age variables above,
# create another variable, multi_format_phrase.
# This should contain the value "Hey {}, are you {age} years old?". Make sure to use the
# format method, and try to use named arguments if you can.
multi_format_phrase = "Hey {}, are you {} years old?".format(friend_name,friend_age)

``` 
## Getting user input with input() method   
```python
input ("Enter your age: ")# input method gets a string 
# we have to concert it into number 
int(user_age)=input("Enter your age: ")
#  I have writed a python file there named age_seconds.py

# This is to calculate age by seconds

def age_seconds(age):
    seconds = int(age)*365*24*16*60
    return  "You have already lived for: {} seconds !".format(seconds)

age=input("Please Enter Your age: ")
seconds=age_seconds(age)
print(seconds)


```

## Format() method example: 
```python
# Ask the user for their name. You can store this in a variable.
NAME = input("What\'s your name?")
# Then, print "Hello, NAME", where NAME is the user's name
print("Hello, {}".format(NAME))
``` 

## Create our own methods in Pyhton 
````python
def age_in_seconds():
user_age = input("Input Your age: ")
print("You have lived for {} seconds ".format(user_age*360*24*60*60))
````
```python
# Create a function, user_name(), that returns the name of a person: "Rolf"
def user_name():
    return "Rolf"

# Create another function, greeting(), that
# takes a name as an argument and returns a greeting phrase:
# "Hello, NAME, how are you?"
def greeting(NAME):
    return "Hello, {}, how are you?".format(NAME)
``` 
```python
### if, elif and for else statement
# The divisible function below takes two numbers and returns whether
# num1 is divisible by num2. For example:
# divisible(6, 2) returns True because 6/2 is 3, with no remainder
# divisible(7, 2) returns False because 7/2 is 3, with 1 remainder
# divisible(14, 4) returns False because 14/4 is 3, with 2 remainder
#
# You do not need to modify the divisible function at all, but 
# you can use it inside the user_even function if you wish.
def divisible(num1, num2):
    return num1 % num2 == 0
 
def user_even():
    # Ask the user for a number.
    # Print "It's even" if the number is even, or "It's odd" otherwise.
    # (make sure to convert the user input to an integer!)
    # You can use the divisible() function if you wish.
    number = input("Enter a number: ")
    int_number = int(number)
    if divisible(int_number, 2):
       print("It's even")
    else:
       print("It's odd")
``` 


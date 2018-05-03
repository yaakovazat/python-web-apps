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


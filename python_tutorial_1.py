"""
 Welcome and introduction
 How to run python:
    - Terminal
    - Write code into a script and run it
    - other ways

 This script demonstrates:
    - comments
    - calcuation
    - variables
    - import 
    - data_structure (List, Map)
"""
###################################################################
# Demonstration for comments, calculation, variables
##################################################################
# How to print text on console. (by the way, this is comments)
print("Here is the print commad. I can print whatever on console.")

# Declare variables (for string and integer):
# integer type variable
a = 2
b = 4

# string type variable
my_name = "Michael"
age = "29"

# Operation
# "+", "-", "*", "/", "%"

# add operation
total_ab = a+b
print(f"(a+b) -> {a} + {b} equals:" + str(a+b)) #or

###################################################################
# TODO:  try "subtraction", "division", "multiplication" and "mode" on your own
# Compute 4321 * 1234, store the result in a variables named "reuslt1"
# Compute dividing 4321 by 1234 and store the result2 in a variables named "result2"
# Compute moding the result2 by 2
###################################################################

# Answer
result1 = 4321 * 1234
result2= 4321 / 1234
result3 = result2%2

###################################################################
# Demonstration for function and imports (random, os) 
# Remark: Maybe we should introduce how to define function here.
##################################################################

#define a function
def sum(num1, num2):
    """write down what it does"""
    sum = num1 + num2
    return sum

#run the function
num1 = 10
num2 = 20
total = sum(num1, num2)


# make use of the imported function "random"
import random
rand_num = random.random()
print(f"This number always different: {rand_num}")

#generate a random number ranged from 1 to 10
begin = 1
end = 10
rand_num = round(random.uniform(begin,end))
print(f"This number always different and ranged in ({begin} to {end}): {rand_num}")

#get current path
import os
print(f"Current path is {os.getcwd()}")

#####################################################################
# TODO: Use random method to generate two number ranged from 100 to 200
#              - Sum up the random numbers
#              - Multiply the random numbers
#
# TODO: Define a function that has two parameters "a and b", return a-b
#####################################################################

# Answer
# assume "import random" is ran
num1 = random.uniform(100,200)
num2 = random.uniform(100,200)
sum_t = num1 + num2
mul_t = num1 * num2

# Answer 
def substract(a, b):
    return a - b 

###################################################################
# Demonstration for List and Map 
##################################################################

#define a list 
list1 = [] # empty list
list2 = [1,2,3,4,5] # list with some pre-defined values

# add new values into list
list1.append(4) # list1 = [4]
# pop the last element of the list
list2.pop() # list2 = [1,2,3,4] because the last element of list2 is poped

print(f"List1 is :{list1}")
print(f"List2 is :{list2}")

#operation, methods applied to list
list_1_and_2 = list1 + list2    # [1] + [1,2,3,4] = [1,1,2,3, 4], appending two list
print(f"List1 + List2 = {list_1_and_2}")

#loop through list
for ele in list_1_and_2:
    print(f"Element:{ele}")

# define a map
map1 = {}
map2 = {"name": "Tom"}

# add new key-value pair into map2
map2["age"] = 20
print(f"map2 is {map2}")

# remove a key-value pair in map2
del map2["name"]
print(f"map2 is {map2}")

# loop through the map
sample_map = {"name":"michael", "age":20}
for key in map2:
    print(f"Name:{key}")
    print(f"Age: {map2[key]}")

#####################################################################
# TODO(LIST): defines a list with 5 random number, loop throught the list and calculate the sum
# TODO(MAP): define a map with keys, "name" and "age" and each key assiciated with empty value
#               - make a prompt to ask user to input "name" and "age"
#               - print out the map
# Remark: for the map task, student need to know "input()"
#####################################################################

# Answer(List)
#1 without function
my_list = []
my_list.append(round(random.uniform(1, 10)))
my_list.append(round(random.uniform(1, 10)))
my_list.append(round(random.uniform(1, 10)))
my_list.append(round(random.uniform(1, 10)))
my_list.append(round(random.uniform(1, 10)))

#2 with function
for i in range(5):
    my_list.append(round(random.uniform(1, 10)))

sum = 0
for ele in my_list:
    sum = sum + ele

print(sum)

# Answer(Map)
my_map = {"name":"", "age": ""}
for key in my_map:
    val = input(f"What is your {key}?\n")
    my_map[key] = val

print(my_map)

# lambda functions
# define a lambda function, namely an anonymous function
lambda x: 2 * x  # any numbers of args but only a single expression

'''
def doubler(x):
    return 2 * x
'''

# invoking a lambda function
(lambda x, y: (x + y) % 2)(1, 5)

# Question 1: Given a person's name as a keyword argument and their height as its value, declare a function tallest_people(). It should print the names of the tallest people along with their heights. If there are several names, sort them alphabetically. Also, pay attention to the output format: Name : height. You are not supposed to handle input or call tallest_people(), just implement this function.

# Sequence of argurements


def func(positional_args, defaults, *args, **kwargs):
    pass

# Solution 1:


def tallest_people(**heights):
    max_height = max(heights.items(), key=lambda x: x[1])
    listOfKeys = list()
    for key, value in heights.items():
        if value == max_height[1]:
            listOfKeys.append(key)
    listOfKeys.sort()
    for ele in listOfKeys:
        print("{} : {}".format(ele, max_height[1]))


tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)

# Solution 2:


def tallest_people(**kwargs):
    tallest = max(kwargs.values())
    for name, height in sorted(kwargs.items()):
        if height == tallest:
            print(name, ':', height)

# Solution 3:


def tallest_people(**kwargs):
    max_tal = max(kwargs.values())
    max_tal_names = sorted(
        (name for name, height in kwargs.items() if height == max_tal))
    print("\n".join((f"{name} : {max_tal}" for name in max_tal_names)))

# Question 2: Select the function call that will NOT return the number 21


def some(x, y, z):
    y = 10
    return x + y + z


positional_args = [10, 10, 1]
keyword_args = {'x': 7, 'y': 8, 'z': 4}

print(some(3, 9, 8))
print(some(*positional_args))
print(**keyword_args)
print(y=11, 2, 9)  # SyntaxError

# Question 3: Implement a function tracklist() to take a dictionary tracks as argument then output the below:
# Woodkid
# ALBUM: The Golden Age TRACK: Run Boy Run
# ALBUM: On the Other Side TRACK: Samara
# Cure
# ALBUM: Disintegration TRACK: Lovesong
# ALBUM: Wish TRACK: Friday I'm in love
# ALBUM: Seventeen Seconds TRACK: A Forest

# Solution:
tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                      "On the Other Side": "Samara"},
          "Cure": {"Disintegration": "Lovesong",
                   "Wish": "Friday I'm in love",
                   "Seventeen Seconds": "A Forest"}}


def tracklist(**kwargs):
    for key, value in kwargs.items():
        print(key)
        for k, v in value.items():
            print("ALBUM: {} TRACK: {}".format(k, v))


tracklist(**tracks)

# Question 4: The merge_arrays(a, b) function, which is partly implemented below, takes two sorted lists of integers, merges them into one sorted list, and returns the result. The function should work in the following way: create an empty list c which will store the result; keep finding the smallest remaining element in a and b and moving it to the list c; stop when there are no elements left in a and b.

# Your task is to fill in the gaps so that the function works correctly. Note, that during the execution any of the lists a and b can become empty, so handle these cases carefully. Try to use non-boolean values in logical expressions when possible.

# Your program shouldn't read any input or call the function, just implement it.

# Hint: The expression in the while loop should check if there are any elements left in a or b.
# The if statement should check if the next element should be taken from list a. This happens in two situations:
# list b is empty;
# both lists are not empty and the first element in a is less than the first element in b.

# Sample Input:
# 1 2 3
# 2 3 4 4
# Sample Output: 1 2 2 3 3 4 4

# Solution:


def merge_arrays(a, b):
    # "c" will contain the result of merging arrays "a" and "b"
    c = []
    while a or b:
        if len(b) == 0 or (len(a) != 0 and len(b) != 0 and a[0] < b[0]):
            # removing the first element from "a" and adding it to "c"
            c.append(a[0])
            a.pop(0)
        else:
            # removing the first element from "b" and adding it to "c"
            c.append(b[0])
            b.pop(0)
    return c

# Question 5: Implement an XOR operator that can work with objects of any type.


The behaviour should be the following:

if the operands are both truthy or both falsy, return False,
if one operand is truthy and the other operand is falsy, return the truthy one.
Write your code inside the xor() function. Your program should not read any input or call the function, your task is to implement it.

# Solution 1 - native:


def xor(a, b):
    # Write your code here
    if (a and b) or ((bool(a) == False and bool(b) == False)):
        return False
    if bool(a) == True and bool(b) == False:
        return a
    if bool(a) == False and bool(b) == True:
        return b

# Solution 2:


def xor(a, b):
    if bool(a) is bool(b):
        return False
    return a or b

# Solution 3:


def xor(a, b):
    if bool(a) == bool(b):
        return False
    else:
        return a or b

# Solution 4:


def xor(a, b):
    return bool(a) != bool(b) and (a or b)


# Question 6: Conversion to boolean - Unknown operation
""" There is a function hidden_operation() which in every test case performs one of the logical operations: and, or and not.

def hidden_operation(operand):
    if oper == "and":
        return operand and hidden_operand
    elif oper == "or":
        return operand or hidden_operand
    elif oper == "not":
        return not operand
You don't have access to oper and hidden_operand variables, but you can call the hidden_operation() function any number of times and pass any objects to it. Your task is to find out which logical operation this function performs and what the hidden_operand is equal to (if the function performs the not operation, you don't have to find the hidden_operand).

Write your code inside the solve() function. In the first line print the name of the logical operation. If the logical operation is and or or, print hidden_operand in the second line.

Your program shouldn't read any input or call the function, just implement it.

Hint

Pass a random non-empty string to the hidden_operation() function. The "not" operator would return False; the "and" operator would return hidden_operand; the "or" operator would return the passed string. If the passed string is complicated enough not to match hidden_operand, this allows you to distinguish the "or" operator from other operators. Then, to distinguish the "and" and "not" operators, pass False to the function. """
# Solution:


def solve():
    if hidden_operation("lalalala") == "lalalala":
        print("or")
        print(hidden_operation(None))
    elif hidden_operation(None):
        print("not")
    else:
        print("and")
        print(hidden_operation("lalalala"))

# Question 7: The code below solves the following problem — having the numerator and the denominator of a fraction, check if the fraction equals 0.5. The program should print True or False. If the denominator equals 0, the answer is False.
# Solution 1:


def compare(numerator, denominator):
    if denominator == 0:
        return False
    else:
        return denominator and numerator / denominator == 0.5


a = int(input())
b = int(input())

print(compare(a, b))

# Solution 2:


def compare(numerator, denominator):
    return bool(denominator) and numerator / denominator == 0.5


a = int(input())
b = int(input())

print(compare(a, b))

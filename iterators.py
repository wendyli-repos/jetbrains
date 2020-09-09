# generator function


import itertools


def multiples(a, n):
    i = 1
    while i <= n:
        yield a*i
        i += 1


print(next(multiples(3, 10)))


# Question 1: Calculate sum of a string with all numbers
# Solution 1:
n = list(map(int, input()))


def predict(n):
    yield sum(n)


print(next(predict(n)))
# Solution 2:
inputs = input()


def get_sum(str):
    sums = 0
    for ele in str:
        yield sums + int(ele)


print(sum((get_sum(inputs))))

# Question 2: Define a generator squares that produces an infinite sequence of the squares of all natural numbers (1, 4, 9, 16, ...). For a given number n, print out the first n elements each on a new line.
# Solution:
n = int(input())


def squares(i):
    yield i ** 2


for n in range(1, n + 1):
    print(next(squares(n)))

# Question 3: Define a generator even that produces even numbers (0, 2, 4, 6, ...). For a given number n, print out the first n ones on separate lines.
# Solution:
n = int(input())


def even(i):
    yield i * 2


for n in range(0, n):
    print(next(even(n)))

# Question 4: Output of the following piece of code


def my_generator():
    i = 0
    while True:
        yield i
        i = i + 1


gen_1 = my_generator()
print(next(gen_1))  # 0
print(next(gen_1))  # 1

gen_2 = my_generator()
print(next(gen_2))  # 0

print(next(gen_1))  # 2

# Question 5: Define a generator letters that would generate letters from a given word one by one.
# Solution 1:
words = input()

# define a generator function


def letters(words):
    for letter in words:
        yield letter


# print generator function
for letter in letters(words):
    print(letter)

# Solution 2:
words = input()
letters = (letter for letter in words)
for letter in letters:
    print(letter)

# Question 6: Fibonacci sequence is a sequence of numbers such that each element is a sum of the previous two, and the first two elements are equal to 0 and 1. Define a generator that produces the Fibonacci sequence of the given length n. Define the generator function called fibonacci.
# Reference: https://stackoverflow.com/questions/8957310/creating-fibonacci-sequence-generator-beginner-python
# Solution 1: print out result as a list
length = int(input())


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(length)))
# Solution 2: print out result in as a string
length = int(input())


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in fibonacci(length):
    print(i)
# Solution 3:


def fib(a=0, b=1):
    """Generator that yields Fibonacci numbers. `a` and `b` are the seed values"""
    while True:
        yield a
        a, b = b, a + b


f = fib()
print(', '.join(str(next(f)) for _ in range(10)))

# iterables and iterators
# This is a list...
my_list = [1, 2, 3]

# ... and this is how we create an iterator from it
my_iterator = iter(my_list)
print(my_iterator)

# <list_iterator object at 0x000001F06D792B70>

print(next(my_iterator))
# 1

print(next(my_iterator))
# 2

print(next(my_iterator))
# 3

print(next(my_iterator))
# StopIteration exception

for item in my_list:
    print(item)

# 1
# 2
# 3

# zip() to "sort of" combine two lists together
# Note that if zip() gets iterables of different lengths, iteration will stop as soon as the shortest iterable is exhausted。
first_names = ['John', 'Anna', 'Tom']
last_names = ['Smith', 'Williams', 'Davis']

for name, last_name in zip(first_names, last_names):
    print(name, last_name)

# John Smith
# Anna Williams
# Tom Davis

# enumerate(), which takes an iterable and returns its elements one by one along with their indexes
months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for n, month in enumerate(months_list):
    print(n + 1, month)

# 1 Jan
# 2 Feb
# 3 Mar
# 4 Apr
# 5 May
# 6 Jun
# etc.

# Question 1: Combine three lists and print in one line
# Solution:
english = ["hello", "thank you"]
spanish = ["hola", "gracias"]
french = ["merci", "bonjour"]

for english, spanish, french in zip(english, spanish, french):
    print(english, spanish, french)

# hello hola bonjour
# thank you gracias merci

# Wrong Solution:
english = ["hello", "thank you"]
spanish = ["hola", "gracias"]
french = ["merci", "bonjour"]

for word in zip(english, spanish, french):
    print(word)

# ('hello', 'hola', 'merci')
# ('thank you', 'gracias', 'bonjour')

# Question 2: Combine two input letter by letter
# Solution:
word1 = input()
word2 = input()

for w1, w2 in zip(word1, word2):
    print("{}{}".format(w1, w2), end="")
    # print(w1+w2, end="")

# Question 3: Return in one line of each month's profit
# Solution:
costs = [100, 200, 300]
revenues = [300, 400, 500]
months = ["jan", "feb", "mar"]

for c, r, m in zip(costs, revenues, months):
    print(m, r-c)

# Question 3: Add correspondece coorinators from two vectors together
# Solution:

v1 = (1, 5)
v2 = (2, 3)
for x, y in zip(v1, v2):
    print(x + y)

# Itertools module
# import itertools

# itertools.chain()
students_maths = ['Ann', 'Kate', 'Tom']
students_english = ['Tim', 'Carl', 'Dean']
students_history = ['Jane', 'Mike']

for student in itertools.chain(students_maths, students_english, students_history):
    print(student)

# itertools.product(), which takes several iterables and returns the elements of their Cartesian product one by one. Cartesian product of several iterables is an iterator of all possible tuples such that the first element is coming from the first argument, the second element is coming from the second argument, and so on.
first_list = ['Hi', 'Bye', 'How are you']
second_list = ['Jane', 'Anton']

# note that these combinations are not stored in memory but produced on-the-fly, only when the for loop asks for a new one.
for first, second in itertools.product(first_list, second_list):
    print(first, second)

# the above itertools.product() can be refactored to below
# for first_item in first_list:
#     for second_item in second_list:
#         print(first_item + " " + second_item)

# Advantage of using itertools.product()
# Trying to create a list containing 10^12 elements will result in a memory error:
too_long_list = list(itertools.product(range(1000000), range(1000000)))

# However, works with iterators:
my_iterator = itertools.product(range(1000000), range(1000000))
for i in range(5):
    print(next(my_iterator))

# (0, 0)
# (0, 1)
# (0, 2)
# (0, 3)
# (0, 4)

# itertools.combinations()
# To generate all possible combinations of any five numbers between 1 and 1000000
my_iter = itertools.combinations(range(1, 1000000), 5)

for i in range(5):
    print(next(my_iter))
# (1, 2, 3, 4, 5)
# (1, 2, 3, 4, 6)
# (1, 2, 3, 4, 7)
# (1, 2, 3, 4, 8)
# (1, 2, 3, 4, 9)

# Question 4: Combine first name with each middle name
# Solution:
first_names = ['Anna', 'Catarina']
middle_names = ['Luisa', 'Maria']
for first, middle in itertools.product(first_names, middle_names):
    print(first, middle)

# Question 5: Choose the three courses combinatation with a total price less then 30
# Solution:
main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

# function to combine dish list with price list to tuple


def merge(list1, list2):
    merged_list = tuple(zip(list1, list2))
    return merged_list


# call function on each course
menu_main_course = merge(main_courses, price_main_courses)
menu_desserts = merge(desserts, price_desserts)
menu_drinks = merge(drinks, price_drinks)
# print(menu_main_course)
# print(menu_desserts)
# print(menu_drinks)

for m, de, dr in itertools.product(menu_main_course, menu_desserts, menu_drinks):
    if m[1] + dr[1] + de[1] <= 30:
        print(m[0], de[0], dr[0], m[1] + dr[1] + de[1])

# the above can be refactored to below:
for m, de, dr in itertools.product(zip(main_courses, price_main_courses), zip(desserts, price_desserts), zip(drinks, price_drinks)):
    sum_ = m[1] + dr[1] + de[1]
    if sum_ <= 30:
        print(m[0], de[0], dr[0], sum_)

# Question 6: Provide matches of one each other using teams names stored in a given list
# Solution:
teams = ['Best-ever', 'Not-so-good', 'Amateurs', "team 4"]
matches = itertools.combinations(teams, 2)


def number_of_matches(n):
    return int(n * (n - 1) / 2)


m = number_of_matches(len(teams))
for _ in range(m):
    print(next(matches))

# the above can be refactored to below:
matches = itertools.combinations(teams, 2)

for match in matches:
    print(match)

# Question 7: Provide different combinatations of bouquets based on numbers of choices of flowers
# Solution:
flower_names = ['rose', 'tulip', 'sunflower']

choices = [1, 2, 3]
for i in choices:
    bouquets = itertools.combinations(flower_names, i)
    for bouquet in bouquets:
        print(bouquet)

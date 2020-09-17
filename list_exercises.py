# list.sort() method performs an in-place sorting, changes the original list, and returns None.
import copy
numbers = [3, 2, 5, 4, 1]
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5]
print(numbers.sort())  # None


# sorted(list)
# sorted(list, reverse=True)

# list.reverse()

# reversed() returns a reverse iterator
print(reversed(numbers))  # <list_reverseiterator object at 0x7fe25e718b70>

numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number)
# 5
# 4
# 3
# 2
# 1


# Question 1: Output the list numbers to descending order numbers = [1, 6, -9, 2.5, 4, 0]. Output: [-9, 0, 1, 2.5, 4, 6]

# Solution 1:
numbers = [1, 6, -9, 2.5, 4, 0]
numbers.sort(reverse=True)
print(numbers)

# Solution 2:
numbers = [1, 6, -9, 2.5, 4, 0]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # [6, 4, 2.5, 1, 0, -9]


# Question 2: Output the list dragons = ['Rudy', 'Targent', 'Aggie'] to ['Targent', 'Aggie', 'Rudy']

# Solution:
dragons = ['Rudy', 'Targent', 'Aggie']
dragons.sort()
print(dragons)
dragons = sorted(dragons, key=len)
print(dragons)
dragons.reverse()
print(dragons)


# Queston 3: Output the list toys = ['Marinet', 'Toby', 'Kitty'] to ['Toby', 'Kitty', 'Chubby', 'Marinet']

# Solution:
toys = "Toby Marinet Chubby Kitty".split()
print(toys)
toys.sort()
print(toys)
toys.reverse()
print(toys)
print(sorted(toys, key=len))


# Question 4: Output the list passwords = ['0vbno0re', 'ad12', 'fgghut', '4qp', 'qwerty'] in asending order of length on each line

# Solution:
passwords = ['0vbno0re', 'ad12', 'fgghut', '4qp', 'qwerty']
passwords.sort(key=len)
for password in passwords:
    print("{} {}".format(password, len(password)))


# Question 5: Below you can see a list of strings called numbers. Sort it in the descending order as strings (alphabetically) and print the resulting list.
# Solution:
numbers = ["77", "145", "987", "2095", "6", "371", "4999", "81"]

# sort numbers
print(sorted(numbers, reverse=True))


# Question 6: Check if an object is hashable
# Solution 1:
# from collections.abc import Hashable
if isinstance(some_object, collections.abc.Hashable):
    print("Hashable")
else:
    print("Not hashable")

# Solution 2:
print("Hashable" if isinstance(some_object,
                               collections.abc.Hashable) else "Not hashable")


# Question 7: Create a program that calculates how many objects in the list object_list have the same hash value as some other element in the list. The output should be the number of those objects. If there are no matching hash values, the output should be 0. For example, if object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397], the output should be 5. Keep in mind that not every object in the list may be hashable!

# Solution:
# from collections.abc import Hashable
# remove not hashable objects
only_hashable = [hash(x) for x in object_list if isinstance(x, Hashable)]
# count occurrence
occurrence = {f'{x}': only_hashable.count(x) for x in only_hashable}
# remove singles
dupes = sum(x for x in occurrence.values() if x > 1)
# print duplicates
print(dupes)

# Question 8: Select all pairs of objects that have the same id.

my_list = [[1], [2, 1]]
list_copy = copy.deepcopy(my_list)
print(id(my_list[0]) == id(list_copy[0]))  # False

print(id(my_list) == id(list_copy))  # False

print(id(my_list[1][0]) == id(list_copy[1][0]))  # True

print(id(my_list[0][0]) == id(list_copy[1][1]))  # True


# Question 9: What is the output?
empty_l = []
empty_l.append(empty_l)

print(empty_l)    # [[...]]
print(empty_l.copy())  # [[[...]]]

# Question 1: Write a function that returns an object whose identity ends with 888. Iterate numbers from 0 to 10 000 and check their identity via id() to find a value ending with ...888.
# Solution:
def object_with_beautiful_identity():
    for i in range(10_000):
        if (str(id(i))).endswith("888"):
            return i

# Question 2: Find the list from a list of lists
# Solution:


def find_my_list(all_lists, my_list):
    for index, lst in enumerate(all_lists):
        # Change the next line
        if lst == my_list:
            return index


# Question 3: Compare two objects with identities or with values
# Solution:
equality_test = silver_haired_twin is raven_haired_twin  # compare with identities
equality_test = silver_haired_twin == raven_haired_twin
# compare with values

# Question 4: Check if some objects can be deepcoplied
# Sample Input 1: 1
# Sample Output 1: False
# Sample Input 2: [2]
# Sample Output 2: True
# Sample Input 3: [1, [3]]
# Sample Output 3: True

# import copy


def solve(obj):
    new_obj = copy.deepcopy(obj)
    if id(new_obj) == id(obj):
        return False
    else:
        return True


# Question 5: The code below solves the following problem: given a list, check if it is sorted. However, this code works incorrectly. For example, it outputs "sorted" for input 2 1 3. Find and correct the mistake.
# Sample Input: 2 1 3
# Sample Output: not sorted
# Solution:
# import copy
# sorting function
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


# where copying takes place
arr = [int(i) for i in input().split()]
arr_deepcopy = copy.deepcopy(arr)
sorted_arr = bubble_sort(arr_deepcopy)

if arr == sorted_arr:
    print('sorted')
else:
    print('not sorted')


# Question 6: Identify which type of copy is created. lst is a predefined list
new = lst  # not a copy
new = lst.copy()  # shallow copy
new = copy.copy(lst)  # shallow copy

# Question 7: You have a list lissst of length 3; it can contain any elements. Select all ways to create a new list which contains the same objects. It means that the id of a new list should differ from the id of lissst, but the ids of its elements should be the same.
# Solution:
my_copy = copy.copy(lissst)  # answer

my_copy = lissst.copy()  # answer

my_copy = [lissst[0], lissst[1], lissst[2]]  # answer

my_copy = copy.deepcopy(lissst)  # not answer

my_copy = lissst  # not answer

# Question 8: Place the commands below in the right order so that by the end of the program, the list fives stays unchanged and my_copy is a deep copy of fives.
# fives = [[[555]]]  # 1
# my_copy = fives    # 2
# ...                # 3
# ...                # 4
# ...                # 5
# Solution:
my_copy = my_copy.copy()
my_copy[0] = my_copy[0].copy()
my_copy[0][0] = my_copy[0][0].copy()

# Question 9: Write a function my_copy(obj) that takes two parameters obj, copy_mode and returns a copy of an object. The value of copy_mode may be either "deep copy", then you should make a deep copy of the given object, or "shallow copy", then your function should return a shallow copy.
# Solution:
# import copy


def my_copy(obj, copy_mode):
    if copy_mode == "deep copy":
        return copy.deepcopy(obj)
    else:
        return copy.copy(obj)

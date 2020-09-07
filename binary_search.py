# Binary search is an efficient algorithm for searching a target element in a sorted list.
# For a list of size nn, the algorithm works in O(\log n)O(logn).
# Iterative implementation
""" def binary_search(elements, target):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == target:
            return middle
        elif target < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1 """

# Recursive implementation

"""
def binary_search(elements, target, left, right):
    print("left start = ", left)
    print("right start = ", right)
    if left > right:
        return -1

    middle = (left + right) // 2
    print("middle = ", middle)

    if elements[middle] == target:
        print(elements[middle])
        return middle
    elif target < elements[middle]:
        print("if target < middle, then left = ", left)
        print("if target < middle, then right = ", right)
        return binary_search(elements, target, left, middle - 1)
    else:
        print("if target > middle, then left = ", left)
        print("if target > middle, then right = ", right)
        return binary_search(elements, target, middle + 1, right)


elements = [7, 10, 15, 16, 20, 25]
indexof_7 = binary_search(elements, 16, left=0, right=len(elements) - 1)  # 0
print(indexof_7)
"""
# bisect module implementation
"""
from bisect import bisect, bisect_left, bisect_right
li = [1, 3, 4, 4, 4, 6, 7]

# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print("The rightmost index to insert, so list remains sorted is  : ", end="")
print(bisect(li, 4))

# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print("The leftmost index to insert, so list remains sorted is  : ", end="")
print(bisect_left(li, 4))

# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print("The rightmost index to insert, so list remains sorted is  : ", end="")
print(bisect_right(li, 4, 0, 4))
"""

# Question 1
""" Write a program that finds the left-most position of a target element in a descending-sorted list.
Input: the first line contains a descending-sorted list of numbers separated by spaces. The second line contains a target element.
Output: the left-most position of the target element in the list or -1−1 if the target element is not found.
Note that this problem can be easily solved using a for loop, but we ask you to implement the algorithm so that you understand it better! """
# Solution 1


input_numbers = [int(n) for n in list(input().split())]
target = int(input())
print(input_numbers)
print(target)


def binary_search(elements, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if elements[middle] == target and elements.index(target) == middle:
        return middle
    elif target < elements[middle]:
        return binary_search(elements, target, left, middle - 1)
    else:
        return binary_search(elements, target, middle + 1, right)


result = binary_search(input_numbers, target, left=0,
                       right=len(input_numbers) - 1)

print(result)

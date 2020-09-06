# Binary search
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

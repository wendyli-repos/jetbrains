# Question 1: Multiple elements with same index in two lists
# Solution:
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]


def my_product(list_1, list_2):
    return list(map(lambda n1, n2: n1 * n2, list_1, list_2))


print(my_product(list_1, list_2))
# Question 2: Filter all negative numbers from a given list
# Solution 1:
z_list = [7, 8, 9, -3, -5, 79, 30]

# if the list contains only numbers


def find_positive(my_list):
    # complete the next line
    return list(filter(lambda x: x > 0, my_list))


print(find_positive(z_list))

# if the list contains string


def find_positive(my_list):
    # complete the next line
    return list(filter(lambda x: x > 0, map(lambda x: int(x), my_list)))


# Question 3:
even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Re-write the rest of the code here using map() and filter() where possible
my_sum = list(map(lambda e, o: e + o, even, odd))

remainders = list(map(lambda x: x % 3, my_sum))

nonzero_remainders = list(filter(lambda x: x > 0, remainders))


# Question 4: Convert Celsius to Fahrenheit
# Solution:
def celsius_to_fahrenheit(c):
    return ((c + 40) * 1.8) - 40


daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]

daily_temp_f = list(map(celsius_to_fahrenheit, daily_temp_c))

temp_above_80 = list(filter(lambda x: x > 80, daily_temp_f))

print(len(temp_above_80))

# Question 5: Check how many students have a total score at least 270
# Solution:
scores_maths = [100, 75, 90, 95, 60, 50, 95, 85, 70, 75,
                90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                95, 45, 60, 45, 80, 70, 55, 45, 60, 90]

scores_physics = [50, 65, 85, 100, 60, 55, 90, 85, 70, 90,
                  50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                  60, 90, 40, 90, 95, 90, 80, 95, 85, 80,
                  95, 90, 75, 50, 80, 70, 50, 35, 65, 90]

scores_english = [50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                  50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                  90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                  50, 65, 85, 100, 60, 55, 90, 85, 70, 90]

overall_scores = list(map(lambda m, p, e: m + p + e,
                          scores_maths, scores_physics, scores_english))

admitted_students = list(filter(lambda s: s >= 270, overall_scores))
print(len(admitted_students))

# Question 6: Take and combined several inputs then covert to Unicode characters.
# Solution 1:
print(''.join([chr(int(input())) for i in range(4)]))
# Solution 2:
word = ''
for _ in range(4):
    word += chr(int(input()))

print(word)

# Question 7: Take input, check if interger code point falls between 32 and 126, both inclusive. If so, then conver and print that character; if not, print False
# Solution:
x = int(input())

print(chr(x) if 32 <= x <= 126 else False)

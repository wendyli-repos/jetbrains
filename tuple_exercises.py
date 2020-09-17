# Question 1: Check which one of below code will occur Error
# # Solution:
tup_of_int = (1, 2, 3)
# new_tup = tup_of_int + 4
new_tup = tup_of_int * 1.3
# tup_of_int.append(4)
# new_tup = tup_of_int * 2
print(new_tup)


# Question 2: Output nested tuple to one tuple
# Solution 1:
hobbies_Adam = ('reading', ('jogging', 'boxing', 'yoga'), 'movies')


def unpack(input_tuple):

    unpacked = ()
    for i in hobbies_Adam:
        if isinstance(i, str):
            unpacked += (i, )
        else:
            for j in i:
                if isinstance(j, str):
                    unpacked += (j,)
    return unpacked


print(unpack(hobbies_Adam))

# Solution 2: could use recussition

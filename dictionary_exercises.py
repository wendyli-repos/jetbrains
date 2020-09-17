# Question 1: Create a dictionary from the list
# Solution:
from collections import namedtuple
from collections import ChainMap
from collections import OrderedDict
from collections import Counter
transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]

transaction_dict = {}
for transcation in transactions:
    key = transcation[0]
    value = transcation[1]
    transaction_dict.setdefault(key, []).append(value)
print(transaction_dict)

# Question 2: Find the mode from input
# Solution:
str1 = "1 7 3 3 8 9 10 5 5 5 4 1 5 6"
# str1 = "red green yellow red orange blue purple"
str1_list = str1.split(" ")

freq_counter = Counter(str1_list)

print(freq_counter.most_common()[0][0])

# Question 3: Check if key is in a dictionary then return the value of that key; if not then return a specific message
# Solution 1:
if word in random_dict.keys():
    print(random_dict[word])
else:
    print("Not in the dictionary")
# Solution 2:
if word in random_dict.keys():
    print(random_dict[word])
else:
    print(random_dict.setdefault(word, "Not in the dictionary"))

# Solution 2 can be refactured into one line
print(random_dict.setdefault(word, "Not in the dictionary"))

# Question 4: Check the word matching most frequents supplied
text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")
text_list = text.split(" ")
freq = int(input())
# print(text_list)
freq_counter = Counter(text_list)
results = freq_counter.most_common(freq)

for result in results:
    result_str = [str(ele) for ele in result]
    print(" ".join(result_str))

# the above for loop can be refactored to below:
'''
for result, freq in results:
    print(result, freq)
'''

# Question 5: Pop the last two items from a ordereddict.
# Solution 1: Convert original dictionary to list then delete last two elements
firms = {"YourHouse": 9.5, "BrownBuildCo": 9.1, "Build in the City": 9.0,
         "mr.Stone & Co": 7.8, "Flinstones Appartment": 7.3}
firms_list = list(firms.items())[0:-2]
print(OrderedDict(firms_list))

# Solution 2: Using OrderedDict.popitem() method to delete last item twice
firms = {"YourHouse": 9.5, "BrownBuildCo": 9.1, "Build in the City": 9.0,
         "mr.Stone & Co": 7.8, "Flinstones Appartment": 7.3}
firms = OrderedDict(firms)
firms.popitem(last=True)
firms.popitem(last=True)  # no need to return, just execute that method twice
print(firms)  # original dictionary is changed

# Question 6: Add an element to an orderedlist and move to first location
results = {"Tom": 98, "Lina": 92, "Natalie": 81}

results["Max"] = 100
results = OrderedDict(results)
results.move_to_end("Max", last=False)
print(results)

# Question 7: Chain up dictiones and adding new child
food_types = {'Vegetables': 15, 'Dairy': 20,
              'Meat': 3, 'Cereals': 9, 'Fruits': 11, 'Fish': 7}
countries = {'USA': 25, 'Australia': 15, 'Canada': 15, 'France': 6, 'India': 4}
discount = {'gold': 20, 'regular': 10}

chain = ChainMap(food_types, countries)
food_types['Sweets'] = 10
countries["USA"] = 35
chain = chain.new_child(discount)

print(chain)

# Question 8: Create a named tuple from based on some data
Student = namedtuple('Student', ['name', 'age', 'department'])

alina = Student("Alina", "22", "linguistics")
# other way to define field values
alex = Student(name="Alex", age="25", department="programming")
kate = Student("Kate", "19", "art")

print(alina)
print(alex)
print(kate)

# Question 9: Get second element in a chainmap
stringed_instruments = {'violin': 5, 'guitar': 7, 'viola': 2, 'banjo': 1}
percussion_instruments = {'castanets': 4, 'drum': 2,
                          'tambourine': 3, 'musical triangle': 1}

band = ChainMap(stringed_instruments, percussion_instruments)
print(band.parents)  # Solution 1
print()
print(band.maps[1])  # Solution 2

# Question 10: What is the output of the following code
person1 = ("James", "Ryan")
person2 = ("Ryan", "James")
person3 = ("Ryan", "James")
age_dict = {}
age_dict[person1] = 36
age_dict[person2] = 27
age_dict[person3] = 42

print(age_dict[person2])

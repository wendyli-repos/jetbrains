# Dictionary
# Operation 1: Get a value from the dictionary by a key
# Method 1, using dict[key]:
from collections import defaultdict
from collections import ChainMap
from collections import namedtuple
testable = {}
testable['key'] = 'value'
print(testable['key'])  # value
print(testable['not_a_key'])  # throws a KeyError

# Method 2, using get():
print(testable.get('key'))  # value
print(testable.get('not_a_key'))  # None
print(testable.get('not_a_key', 'default'))  # default

# Operation 2: Delete (remove from a dictionary) a value by its key
testable = {'key1': 'value1', 'key2': 'value2'}
# this will remove both the key and the value from dictionary object
del testable['key1']
print(testable)  # {'key2': 'value2'}
del testable['not_a_key']  # throws a KeyError
# throws a KeyError as we've already deleted the object by the key
del testable['key1']
del testable  # deletes the whole dictionary

# Operation 3: check if a specific item is in a dictionary
catalog = {'green table': 5000, 'brown chair': 1500,
           'blue sofa': 15000, 'wardrobe': 10000}
print('blue sofa' in catalog)    # True
print('yellow chair' in catalog)    # False
# Note that the membership operator looks for keys, not values
print(1500 in catalog)    # False

# Operation 4: Iterating over dictionary
# keys, values, items
tiny_dict = {'a': 1, 'b': 2, 'c': 3}

print(tiny_dict.keys())  # dict_keys(['a', 'b', 'c'])
print(tiny_dict.values())
print(tiny_dict.items())

for key in tiny_dict:
    print(key)

for value in tiny_dict.values():
    print(value)  # 1

for key, value in tiny_dict.items():
    print(value == tiny_dict[key])

# Operation 5: collections.OrderedDict to create a dictionary like object
# create an ordered list
# Method 1: this is the constructor
marks = OrderedDict()
marks['Smith'] = 9.5
marks['Brown'] = 8.1
marks['Moore'] = 7.4
print(marks)  # OrderedDict([('Smith', 9.5), ('Brown', 8.1), ('Moore', 7.4)])

# Method 2: this is the conversion
my_dict = {'Smith': 9.5, 'Brown': 8.1, 'Moore': 7.4}
my_ord_dict = OrderedDict(my_dict)
# OrderedDict([('Smith', 9.5), ('Brown', 8.1), ('Moore', 7.4)])
print(my_ord_dict)

# popitem()
# OrderedDict([('Smith', 9.5), ('Brown', 8.1), ('Moore', 7.4)])
print(my_ord_dict)

my_ord_dict.popitem(last=True)   # ('Moore', 7.4)
print(my_ord_dict)  # OrderedDict([('Smith', 9.5), ('Brown', 8.1)])

my_ord_dict.popitem(last=False)  # ('Smith', 9.5)
print(my_ord_dict)  # OrderedDict([('Brown', 8.1)])

# move_to_end()
# OrderedDict([('Smith', 9.5), ('Brown', 8.1), ('Moore', 7.4)])
print(my_ord_dict)

my_ord_dict.move_to_end('Brown', last=False)
# OrderedDict([('Brown', 8.1), ('Smith', 9.5), ('Moore', 7.4)])
print(my_ord_dict)

my_ord_dict.move_to_end('Smith', last=True)
# OrderedDict([('Brown', 8.1), ('Moore', 7.4), ('Smith', 9.5)])
print(my_ord_dict)

# comparation
regular_dict_1 = {'Smith': 9.5, 'Brown': 8.1, 'Moore': 7.4}
regular_dict_2 = {'Brown': 8.1, 'Moore': 7.4, 'Smith': 9.5}
ordered_dict_1 = OrderedDict(regular_dict_1)
ordered_dict_2 = OrderedDict(regular_dict_2)

print(regular_dict_1 == regular_dict_2)  # True
print(ordered_dict_1 == ordered_dict_2)  # False

# Opertation 6: collections.namedtuple is a factory function to make subtypes of tuples with named elements

# the subclass is named 'Person' in our case
person = namedtuple('Person', ['name', 'age', 'occupation'])
person = namedtuple('person', 'name, age, occupation')
person = namedtuple('person', 'name age occupation')

# field values can be defined either positionally or using the field names
mary = person('Mary', '25', 'doctor')
david = person(name='David', age='33', occupation='lawyer')

print(mary.name)   # Mary
print(david)       # person(name='David', age='33', occupation='lawyer')
# the elements can also be accessed by their index, as in a regular tuple
print(david[2])    # lawyer

# A new named tuple can also be created from a list:
susanne = person._make(['Susanne', '23', 'journalist'])
print(susanne)  # person(name='Susanne', age='23', occupation='journali
# to replace field values with new ones, and we can see what fields are present in it
# a new object is created instead of changing the existing one
mary = mary._replace(age='26')
print(mary)          # person(name='Mary', age='26', occupation='doctor')
print(mary._fields)  # ('name', 'age', 'occupation')

# get an ordered dictionary out of named tuples
susanne_info = susanne._asdict()
# OrderedDict([('name', 'Susanne'), ('age', '23'), ('occupation', 'journalist')])
print(susanne_info)

# Opertation 7: collections.ChainMap
laptop_labels = {'Lenovo': 600, 'Dell': 2000, 'Asus': 354}
operating_system = {'Windows': 2500, 'Linux': 400, 'MacOS': 54}
chain = ChainMap(laptop_labels, operating_system)
# ChainMap({'Lenovo': 600, 'Dell': 2000, 'Asus': 354}, {'Windows': 2500, 'Linux': 400, 'MacOS': 54})
print(chain)

operating_system['Linux'] = 450  # changing a value in a dictionary
print(chain['Linux'])            # 450

processor = {'Celeron': 600, 'Pentium': 2000, 'Ryzen 5': 354}
new_chain = chain.new_child(processor)
# ChainMap({'Celeron': 600, 'Pentium': 2000, 'Ryzen 5': 354}, {'Lenovo': 600, 'Dell': 2000, 'Asus': 354}, {'Windows': 2500, 'Linux': 400, 'MacOS': 54})
print(new_chain)

# The maps method allows you to get access to a certain dictionary by its index:

# ChainMap({'Lenovo': 600, 'Dell': 2000, 'Asus': 354}) which is a new object. Needed to be assigned to a variable if want to work with them further
print(new_chain.maps[1])

# ChainMap({'Celeron': 600, 'Pentium': 2000, 'Ryzen 5': 354}, {'Lenovo': 600, 'Dell': 2000, 'Asus': 354}, {'Windows': 2500, 'Linux': 400, 'MacOS': 54})
print(new_chain)
without_first = new_chain.parents
# ChainMap({'Lenovo': 600, 'Dell': 2000, 'Asus': 354}, {'Windows': 2500, 'Linux': 400, 'MacOS': 54})
# Needed to be assigned to a variable if want to work with them further
print(without_first)

# Opertation 8: collections.defaultdict, defaultdict is a dictionary-like object defined in collections

# int is a default_factory para, which should be a function-like object that determins the type or the value of the para. Do not call int()
freq_defaultdict = defaultdict(int)

for word in text_list:
    freq_defaultdict[word] += 1

print(freq_defaultdict["chess"])  # 1

print(freq_defaultdict["python"])  # 0

# Opertation 9: collections.Counter is a dictionary-like object used specifically for counting the elements of an iterable object.
rom collections import Counter

freq_counter = Counter(text_list)

print(freq_counter)
# Counter({'a': 3, 'in': 2, 'or': 2, 'gambit': 1, 'is': 1, 'chess': 1, 'opening': 1,
# 'which': 1, 'player': 1, 'risks': 1, 'one': 1, 'more': 1, 'pawns': 1, 'minor': 1,
# 'piece': 1, 'to': 1, 'gain': 1, 'an': 1, 'advantage': 1, 'position': 1})
print(freq_counter["alpaca"])  # 0

# most_common(n) method which returns a list of tuples of n most common elements with their counts. If n isn't specified, all elements are returned in the descending order of their frequencies.
print(freq_counter.most_common(5))
# [('a', 3), ('in', 2), ('or', 2), ('gambit', 1), ('is', 1)]
print(freq_counter.most_common())
# [('a', 3), ('in', 2), ('or', 2), ('gambit', 1), ('is', 1), ('chess', 1), ('opening', 1),
# ('which', 1), ('player', 1), ('risks', 1), ('one', 1), ('more', 1), ('pawns', 1),
# ('minor', 1), ('piece', 1), ('to', 1), ('gain', 1), ('an', 1), ('advantage', 1), ('position', 1)]


# Opertation 10: dict.setdefault()
# long string with text
text = ("Gambit is a chess opening in which a player risks one or more pawns "
        "or a minor piece to gain an advantage in position")

# convert text to list of words
text_list = text.lower().split()
# create empty dictionary
freq_dict = {}

# loop through text and count words
for word in text_list:
    # set the default value to 0
    freq_dict.setdefault(word, 0)
    # increment the value by 1
    freq_dict[word] += 1
# examples
print(freq_dict["gambit"])  # 1
print(freq_dict["a"])  # 3

index_dict = {}
for index, word in enumerate(text_list):
    index_dict.setdefault(word, []).append(index)
# example
print(index_dict["or"])  # [11, 14]

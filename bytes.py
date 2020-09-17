# bytes
# ord() accepts as an argument a string consisting of a single Unicode character, and returns an integer equal to the code point assigned to this character in the Unicode
a_character = 'a'
a_code = ord(a_character)
print(a_code)               # The output is 97

# chr() in a similar manner allows you to convert an integer to the corresponding Unicode character.
a_character = 'a'
a_character = chr(a_code)
print(a_character)          # The output is 'a'

# Creating bytes
# Method 1 - Universal, anything to bytes: b prefix, this works only for characters that can be encoded by a single byte, i.e. characters whose Unicode code point lies between 0 and 255 inclusively: ASCII and extended ASCII characters.
hello = b'hello bytes'
print(hello)  # b'hello bytes'

chinese_hello = b'你好，世界'  # SyntaxError
# Method 2 - Unversial, anything to bytes: bytes(), whose arguments are the string to be converted and the name of the output encoding
chinese_hello = bytes('你好，世界', encoding='utf-8')
# b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c'
print(chinese_hello)

# if need only characters whose Unicode code points lie between 0 and 255, the same function bytes() can do the job. It takes a list of integers between 0 and 255 and converts them to a bytes sequence
int_to_bytes = bytes([104, 105])
print(int_to_bytes)  # b'hi'

zero_bytes = bytes(4)
# b'\x00\x00\x00\x00', a string of zero bytes and has the length equal to the specified integer
print(zero_bytes)

# bytearray()

# Method 3 - String to bytes: encode()
chinese_hello = '你好，世界'.encode()
chinese_hello_enc = '你好，世界'.encode('utf-8')
print(chinese_hello == chinese_hello_enc)  # True

# Method 4: Integers to bytes: to_bytes()
# Two arguments, apart from the integer itself, are required: the number of bytes to be used for representing the integer, and the byteorder, either 'little' or 'big', specifying the order in which the bytes should be printed: from the least significant byte to the most significant one in case of 'little', vice versa for 'big'.
first_number = (100).to_bytes(1, byteorder='little')
print(first_number)  # b'd'

second_number = (1024).to_bytes(2, byteorder='little')
print(second_number)  # b'\x00\x04'

third_number = (1024).to_bytes(2, byteorder='big')
print(third_number)  # b'\x04\x00'

# Converting bytes to strings:
# Method 1 - bytes to any encoding: str()
bye_bytes = b'bye bytes'
hello_str = str(bye_bytes, encoding='utf-8')  # must specify encoding type
# Method 2 - bytes to default encoding "utf-8"
hello_another_str = bye_bytes.decode()
print(hello_str == hello_another_str)  # True

# Converting bytes to integers
int_to_bytes = (1024).to_bytes(2, 'little')
print(int_to_bytes)  # b'\x00\x04'

bytes_to_int = int.from_bytes(int_to_bytes, 'little')
print(bytes_to_int)  # 1024

# Qyestion 1: Convert a given number to a byte objects and output the sum of the bytes. (the test numbers are going to be greater than 255, so you're going to need at least 2 bytes to encode them.)
# Solution:
n = int(input())
print(sum((n).to_bytes(2, 'little')))

# Question 2: Write a code that converts the given string to a bytes object and outputs its last item.
# Solution:
byte_string = bytes(input(), encoding='utf-8')
print(byte_string[-1])

# Question 3: The first input line is an encoded message, and the second line is the key integer number. Convert the key to two bytes and sum up its items. Then add the resulting sum to the code point of each character in the message. Finally, print the decoded message.
# Solution:
# Sample Input 1:
# HlAdghmcXnt
# 256
# Sample Output 1:
# ImBehindYou

msg = input()
key_ = input()

key_byte = sum((int(key_)).to_bytes(2, 'little'))

for i in msg:
    i = ord(i) + key_byte
    print(chr(i), end="")

# Question 4: Create a bytes object of the length 5 filled with zero bytes and save it to a variable zero_bytes defined below.
# Solution:
zero_bytes = bytes(5)

# String Operations:
# 1. Length of a String (len(string)):
my_string = "Hello, World!"
length = len(my_string)
print("Length of the string:", length)  # Output: 13

# 2. Iterating Over Characters (for character in string):
my_string = "Hello"
for char in my_string:
   print(char)
# Output:
# H
# e
# l
# l
# o

# 3. Checking for Substring (if substring in string):
my_string = "Hello, World!"
if "World" in my_string:
   print("Substring 'World' found!")
# Output: Substring 'World' found!

# 4. Accessing Characters by Index (string[i]):
my_string = "Python"
char = my_string[2]  # Accessing the character at index 2 (zero-based index)
print("Character at index 2:", char)  # Output: Character at index 2: t

# 5. Accessing Substrings (string[i:j]):
my_string = "Python Programming"
substring = my_string[7:18]  # Accessing substring from index 7 to 17
print("Substring:", substring)  # Output: Substring: Programming

# String Methods:
# # 1. Converting to Lowercase (string.lower()):
my_string = "Hello World"
lowercase_string = my_string.lower()
print("Lowercase:", lowercase_string)  # Output: Lowercase: hello world

# 2. Converting to Uppercase (string.upper()):
my_string = "Hello World"
uppercase_string = my_string.upper()
print("Uppercase:", uppercase_string)  # Output: Uppercase: HELLO WORLD

# 3. Removing Leading Whitespace (string.lstrip()):
my_string = "   Python"
stripped_string = my_string.lstrip()
print("Stripped:", stripped_string)  # Output: Stripped: Python

# 4. Removing Trailing Whitespace (string.rstrip()):
my_string = "Python   "
stripped_string = my_string.rstrip()
print("Stripped:", stripped_string)  # Output: Stripped: Python

# 5. Removing Both Leading and Trailing Whitespace (string.strip()):
my_string = "   Python   "
stripped_string = my_string.strip()
print("Stripped:", stripped_string)  # Output: Stripped: Python

# 6. Counting Substrings (string.count(substring)):
my_string = "The quick brown fox jumps over the lazy dog."
count = my_string.lower().count("the")
print("Count of 'the':", count)  # Output: Count of 'the': 2

# 7. Checking if Numeric (string.isnumeric()):
numeric_string = "12345"
is_numeric = numeric_string.isnumeric()
print("Is numeric?", is_numeric)  # Output: Is numeric? True

# 8. Checking if Alphabetic (string.isalpha()):
alphabetic_string = "Hello"
is_alpha = alphabetic_string.isalpha()
print("Is alphabetic?", is_alpha)  # Output: Is alphabetic? True

# 9. Splitting by Whitespace (string.split()):
my_string = "This is a sentence."
words = my_string.split()
print("Split by whitespace:", words)
# Output: Split by whitespace: ['This', 'is', 'a', 'sentence.']

# 10. Splitting by Custom Delimiter (string.split(delimiter)):
my_string = "apple,banana,cherry"
fruits = my_string.split(",")
print("Split by comma:", fruits)
# Output: Split by comma: ['apple', 'banana', 'cherry']

# 11. Replacing Substrings (string.replace(old, new)):
my_string = "Hello, World!"
new_string = my_string.replace("World", "Python")
print("Replaced:", new_string)  # Output: Replaced: Hello, Python!

# 12. Joining Strings from a List (delimiter.join(list of strings)):
my_list = ["Hello", "World", "Python"]
joined_string = ", ".join(my_list)
print("Joined:", joined_string)  # Output: Joined: Hello, World, Python

# 13. String Formatting (string.format()):
name = "Alice"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)
# Output: My name is Alice and I am 30 years old.

# 14. String Formatting with Decimal Places ({:.2f}):
price = 12.3456789
formatted_price = "Price: {:.2f}".format(price)
print(formatted_price)
# Output: Price: 12.35 (rounded to 2 decimal places)


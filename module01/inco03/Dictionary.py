# Common dictionary operations
my_dict = {"name": "Alice",
           "age": 30,
           "city": "New York"}

# Length of the dictionary
print(len(my_dict))  # Output: 3

# Iterating over keys
for key in my_dict:
    print(key, end=" ")  # Output: name age city
print()

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 30
# city: New York

# Checking for a key
print("name" in my_dict)  # Output: True
print("gender" in my_dict)  # Output: False

# Accessing values by key
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])  # Output: 30

# Setting a value for a key
my_dict["occupation"] = "Engineer"
print(my_dict)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}

# Deleting a key-value pair
del my_dict["age"]
print(my_dict)
# Output: {'name': 'Alice', 'city': 'New York', 'occupation': 'Engineer'}

# Dictionary methods:
print(my_dict.get("name", "Unknown"))
# Output: Alice

# Print keys
print(my_dict.keys())
# Output: dict_keys(['name', 'city', 'occupation'])

# Print values
print(my_dict.values())
# Output: dict_values(['Alice', 'New York', 'Engineer'])

# Appending to a list value
my_dict["skills"] = ["Python", "Java", "SQL"]
print(my_dict)
# Output: {'name': 'Alice', 'city': 'New York', 'occupation': 'Engineer', 'skills': ['Python', 'Java', 'SQL']}

# Updating with another dictionary
my_dict.update({"age": 35, "city": "San Francisco"})
print(my_dict)
# Output: {'name': 'Alice', 'city': 'San Francisco', 'occupation': 'Engineer', 'skills': ['Python', 'Java', 'SQL'], 'age': 35}

# Clearing the dictionary
my_dict.clear()
print(my_dict)
# Output: {}

# Creating a copy of the dictionary
my_copy = my_dict.copy()
print(my_dict)
# Output: {}
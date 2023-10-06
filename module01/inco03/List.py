# Create a list
my_list = [1, 2, 3, 4, 5]
# Create a tuple
my_tuple = (6, 7, 8, 9, 10)

# Length of the list & tuple
print(len(my_list))  # Output: 5
print(len(my_tuple))  # Output: 5

# Iterate over the elements
for element in my_list:
    print(element, end=" ")
# Output: 1 2 3 4 5

# Check if an element is in the list
if 3 in my_list:
    print("\n3 is in the list")
# Output: 3 is in the list

# Access an element by index
element_at_index = my_list[2]
print("Element at index 2:", element_at_index)
# Output: Element at index 2: 3

# Access a slice of the list
my_slice = my_list[1:4]
print("Slice:", my_slice)
# Output: Slice: [2, 3, 4]

# Iterate over indices and elements
for index, element in enumerate(my_list):
    print(f"Index {index}: {element}")
# Output:
# Index 0: 1
# Index 1: 2
# Index 2: 3
# Index 3: 4
# Index 4: 5

# Replace an element at a specific index
my_list[2] = 6
print("Updated list:", my_list)
# Output: Updated list: [1, 2, 6, 4, 5]

# Append an element to the end
my_list.append(7)
print("Appended list:", my_list)
# Output: Appended list: [1, 2, 6, 4, 5, 7]

# Insert an element at a specific index
my_list.insert(1, 8)
print("Inserted list:", my_list)
# Output: Inserted list: [1, 8, 2, 6, 4, 5, 7]

# Remove and return an element at a specific index
removed_element = my_list.pop(3)
print("Removed element:", removed_element)
# Output: # Removed element: 6


# Remove the first occurrence of a value
my_list.remove(2)
print("List after removing 2:", my_list)
# Output: List after removing 2: [1, 8, 4, 5, 7]

# Sort the list
my_list.sort()
print("Sorted list:", my_list)
# Output: Sorted list: [1, 4, 5, 7, 8]

# Reverse the list
my_list.reverse()
print("Reversed list:", my_list)
# Output: Reversed list: [8, 7, 5, 4, 1]

# Clear all items in the list
my_list.clear()
print("Cleared list:", my_list)
# Output: Cleared list: []

# Create a copy of the list
original_list = [1, 2, 3]
copy_list = original_list.copy()
print("Copy of the list:", copy_list)
# Output: Copy of the list: [1, 2, 3]

# Extend the list with another list
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print("Extended list:", my_list)
# Output: Extended list: [1, 2, 3, 4, 5, 6]

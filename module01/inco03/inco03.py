# Strings

s1 = "         ,,,Hi a 3 4 ll!       "
s1 = s1.replace("!", "?").replace("3", "5").replace("Hi", "Hello").upper().lower().capitalize().strip()
print(s1)

# Write a function called text_analyzer that performs the following tasks on a given text:
#
# Calculate and display the total number of characters in the text (including spaces).
# Calculate and display the total number of words in the text. Words are separated by spaces.
# Calculate and display the total number of sentences in the text. Sentences end with '.'
# Calculate and display the total number of paragraphs in the text. Paragraphs are separated by two or more consecutive newline characters ('\n\n').
# Display the longest word in the text.
# Display the most frequent word in the text.
# Display the text with:
#   1. first sentence to lowercase
#   2. the last to uppercase
#   3. most frequent word capitilize
#   4. longest word to uppercase

text = """Cupcake ipsum dolor sit amet cupcake. Jelly cupcake tart apple pie liquorice cake wafer chocolate. Cookie halvah caramels pastry tart.

Gingerbread brownie cake jelly cake wafer dessert. Candy canes gummi bears I love I love cupcake tiramisu brownie. Gummi bears brownie oat cake pastry I love jelly sesame snaps jelly jujubes. Sugar plum brownie brownie chocolate bar tiramisu powder cake.

Croissant tiramisu macaroon sesame snaps jelly beans. Cheesecake candy I love brownie macaroon apple pie cotton candy dragée. Gingerbread cookie carrot cake cookie biscuit macaroon dragée.

Macaroon fruitcake marzipan cake powder I love tootsie roll. I love donut bonbon icing cookie. Tootsie roll toffee chocolate cake chocolate bar croissant marzipan I love chocolate. Icing dragée sugar plum wafer lemon drops.

Bear claw donut wafer shortbread cake pudding marshmallow macaroon muffin. Ice cream cupcake muffin lemon drops cheesecake. Marshmallow gummi bears pudding chocolate bar dragée shortbread sugar plum.
"""

def text_analyzer(text):
    # Calculate and display the total number of characters
    total_chars = len(text)
    print("Total characters:", total_chars)

    # Calculate and display the total number of words

    words = text.replace("\n\n", " ").split(" ")
    total_words = len(words)
    print("Total words:", total_words)

    # Calculate and display the total number of sentences
    total_sentences = text.count(".")
    print("Total sentences:", total_sentences)

    # Calculate and display the total number of paragraphs
    paragraphs = text.split("\n\n")
    total_paragraphs = len(paragraphs)
    print("Total paragraphs:", total_paragraphs)

    # Find the longest word
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)

    # Find the most frequent word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    most_frequent_word = max(word_count, key=word_count.get)
    print("Most frequent word:", most_frequent_word)

    # Display the text with:
    # 1. first sentence to lowercase
    # 2. the last to uppercase
    # 3. most frequent word capitilize
    # 4. longest word to uppercase
    sentences = [sentence.strip() for sentence in text.split(".") if sentence.strip()]
    first_sentence = sentences[0]
    last_sentence = sentences[-1]
    modified_text = text.replace(first_sentence, first_sentence.lower()).replace(last_sentence, last_sentence.upper()).replace(most_frequent_word, most_frequent_word.capitalize()).replace(longest_word, longest_word.upper())
    print("Modified text: " + modified_text)


text_analyzer(text)

# Lists

# # Write a function called list_operations that performs the following tasks with lists:
#
# Create an empty list called my_list.
# Add the numbers from 1 to 10 (inclusive) to my_list & print it.
# Print the sum of all the numbers in my_list
# Find and print the largest number in my_list.
# Find and print the smallest number in my_list.
# Remove the number 5 from my_list and print my_list.
# Reverse the order of elements in my_list and print it.
# Create a new list called squared_list containing the square of each number in my_list & print the elements of squared_list.
# Check if the number 100 is in squared_list and print the result.
# Append my_list to the end of squared_list & print squared_list.
# Clear all elements from my_list & print the final state of my_list.

def list_operations():
    # Create an empty list called my_list
    my_list = []

    # Add numbers from 1 to 10 to my_list
    my_list.extend(range(1, 11))
    print(my_list)

    # Print the sum of all numbers in my_list
    print("Sum of my_list:", sum(my_list))

    # Find and print the largest number in my_list
    print("Largest number in my_list:", max(my_list))

    # Find and print the smallest number in my_list
    print("Smallest number in my_list:", min(my_list))

    # Remove the number 5 from my_list
    my_list.remove(5)
    print(my_list)

    # Reverse the order of elements in my_list
    my_list.reverse()
    print(my_list)

    # Create a new list squared_list containing the square of each number in my_list
    squared_list = [x ** 2 for x in my_list]
    print(squared_list)

    # Check if the number 100 is in squared_list and print the result
    print("Is 100 in squared_list?", 100 in squared_list)

    # Append my_list to the end of squared_list
    squared_list.append(my_list)
    print("squared_list after appending my_list:", squared_list)

    # Clear all elements from my_list
    my_list.clear()
    print("Final state of my_list:", my_list)


list_operations()


# Dictionaries

# Shopping list
# Represent the following products with their prices:
#
# Product	Price
# Milk	1.07
# Rice	1.59
# Eggs	3.14
# Cheese	12.60
# Chicken Breasts	9.40
# Apples	2.31
# Tomato	2.58
# Potato	1.75
# Onion	1.10
# Represent Bob's shopping list:
#
# Product	Amount
# Milk	3
# Rice	2
# Eggs	2
# Cheese	1
# Chicken Breasts	4
# Apples	1
# Tomato	2
# Potato	1
# Represent Alice's shopping list:
#
# Product	Amount
# Rice	1
# Eggs	5
# Chicken Breasts	2
# Apples	1
# Tomato	10
# Create an application which prints out the answers to the following questions:
#
# How much does Bob pay?
# How much does Alice pay?
# Who buys more Rice?
# Who buys more Potato?
# Who buys more Ham?
# Who buys more Apples?
# Who buys more of different products?
# Who buys more items? (more pieces)
# The full output of your main method should be the following:
#
# 72.09
# 64.2
# Bob
# Bob
# no one
# no one
# Bob
# Alice

# Create a dictionary with product prices
product_dictionary = {
    "Milk": 1.07, "Rice": 1.59, "Eggs": 3.14,
    "Cheese": 12.60, "Chicken Breasts": 9.40, "Apples": 2.31,
    "Tomato": 2.58, "Potato": 1.75, "Onion": 1.10
}

# Create dictionaries for Bob and Alice's shopping lists
bob_dictionary = {
    "Milk": 3, "Rice": 2, "Eggs": 2, "Cheese": 1,
    "Chicken Breasts": 4, "Apples": 1, "Tomato": 2, "Potato": 1
}

alice_dictionary = {
    "Rice": 1, "Eggs": 5, "Chicken Breasts": 2,
    "Apples": 1, "Tomato": 10
}

def calculate_payment(my_dictionary, product_dictionary):
    total_payment = 0
    for product, quantity in my_dictionary.items():
        if product in product_dictionary:
            total_payment += quantity * product_dictionary[product]
    return total_payment

# Calculate and print how much Bob and Alice pay
bob_payment = calculate_payment(bob_dictionary, product_dictionary)
alice_payment = calculate_payment(alice_dictionary, product_dictionary)
print("How much does Bob pay?", bob_payment)
print("How much does Alice pay?", alice_payment)

def who_buys_more(bob_dictonary, alice_dictonary, product):
    bob_quantity= bob_dictonary.get(product, 0)
    alice_quantity = alice_dictonary.get(product, 0)

    if bob_quantity > alice_quantity:
        return "Bob"
    elif bob_quantity < alice_quantity:
        return "Alice"
    else:
        return "no one"

# Check who buys more of specific products and print the results
# Rice
print(who_buys_more(bob_dictionary, alice_dictionary, "Rice"))
# Potato
print(who_buys_more(bob_dictionary, alice_dictionary, "Potato"))
# Ham
print(who_buys_more(bob_dictionary, alice_dictionary, "Ham"))
# Apples
print(who_buys_more(bob_dictionary, alice_dictionary, "Apples"))

# Compare who buys more different products and who buys more items (more pieces)

if len(bob_dictionary) > len(alice_dictionary):
    print("Bob")
else:
    print("Alice")

if sum(bob_dictionary.values()) > sum(alice_dictionary.values()):
    print("Bob")
else:
    print("Alice")


import re

# Create a function that reads a text file containing data from various sources and performs the following tasks using
# regular expressions:
#
# Matching Email Addresses: Read the text file and extract all valid email addresses present in the file.
# Valid email addresses should follow the standard format (e.g., user@example.com).
#
# Extracting Phone Numbers: Extract all valid phone numbers from the text file.
# Valid phone numbers should match common formats like (123) 456-7890 or 123-456-7890.
#
# Replacing Dates: Replace all dates in the format MM/DD/YYYY with YYYY-MM-DD.
#
# Finding URLs: Find and extract all URLs from the text file, including both HTTP
# and HTTPS URLs. URLs can start with http://, https://, or www..
#
# Identifying IP Addresses: Identify and extract all valid IPv4 addresses from the text file.
#
# Extracting HTML Tags: Extract all HTML tags (e.g., <p>, <a href="https://example.com">) from the text file.
#
# Save all results to a new .txt file with the following format:
#
# Email Addresses:
# john.doe@example.com
#
# Phone Numbers:
# (123) 456-7890
#
# Dates:
# 2022-01-15
#
# URLs:
# https://www.example.com
#
# IP Addresses:
# 192.168.1.1
#
# HTML Tags: (Optional)
# <p>
# </p>

# ^([\w .-]+), ([\w .-]+)$

text = "Doe, John MiddleName"

pattern = r'^([\w .-]+), ([\w .-]+)$'

match = re.match(pattern, text)

if match:
    name = match.group(2)
    surname = match.group(1)
    name_parts = name.split()

    if len(name_parts) >= 2:
        name = name_parts[0]
        middle_name = name_parts[1]
    else:
        middle_name = ""

    print("First Name: " + name)
    print("Middle Name: " + middle_name)
    print("Last Name: " + surname)

else:
    print("No match")

text = "cabcccdecc"

patter_star = r'c*'
match_star = re.findall(patter_star, text)
print(match_star)

patter_plus = r'c+'
match_plus = re.findall(patter_plus, text)
print(match_plus)

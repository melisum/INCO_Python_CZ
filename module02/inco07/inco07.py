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


def process_text_file(input_file_path, output_file_path):
    email_addresses = []
    phone_numbers = []
    dates = []
    urls = []
    ip_addresses = []
    html_tags = []

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    date_pattern = r'(\d{2}/\d{2}/\d{4})'
    url_pattern = r'https?://\S+|www\.\S+'
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    html_tag_pattern = r'<[^>]*>'

    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        email_addresses = re.findall(email_pattern, content)
        phone_numbers = re.findall(phone_pattern, content)
        dates = re.findall(date_pattern, content)
        urls = re.findall(url_pattern, content)
        ip_addresses = re.findall(ip_pattern, content)
        html_tags = re.findall(html_tag_pattern, content)

    dates = [date.replace('/', '-') for date in dates]

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("Email Addresses:\n")
        output_file.write("\n".join(email_addresses) + "\n\n")

        output_file.write("Phone Numbers:\n")
        output_file.write("\n".join(phone_numbers) + "\n\n")

        output_file.write("Dates:\n")
        output_file.write("\n".join(dates) + "\n\n")

        output_file.write("URLs:\n")
        output_file.write("\n".join(urls) + "\n\n")

        output_file.write("IP Addresses:\n")
        output_file.write("\n".join(ip_addresses) + "\n\n")

        output_file.write("HTML Tags:\n")
        output_file.write("\n".join(html_tags) + "\n\n")


# Example usage:
process_text_file("input.txt", "output.txt")

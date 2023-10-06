import csv
from collections import Counter


# Create a function that:
#
# Takes the name of a CSV file as a parameter,
# Where each row is in the following format: <last name first name>;<birthdate in YYYY-MM-DD format>;<city name>,
# Returns the 5 most common first names of people born between 2000 and 2023,
# Writes the first names to a text file, with each name on a new line.
# The expected result should be: Benjamin Emma Noah Isabella Ava

def get_top_5_common_names(input_file, output_file):
    try:
        name_counter = Counter()
        with open(input_file, 'r', newline="") as csv_file:
            reader = csv.reader(csv_file, delimiter=';')

            for row in reader:
                full_name = row[0].split()
                first_name = full_name[-1]
                birth_year = int(row[1].split('-')[0])

                if 2000 <= birth_year <= 2023:
                    name_counter[first_name] += 1

        top_5_names = name_counter.most_common(5)

        with open(output_file, 'w') as output:
            for name, count in top_5_names:
                output.write(name + '\n')

        return top_5_names

    except FileNotFoundError:
        return "File not found"


result = get_top_5_common_names("people.csv", "top.txt")
if result == "File not found":
    print(result)
else:
    print("The 5 most common first names of people born between 2000 and 2023 are:")
    for name, count in result:
        print(f"{name} : {count}")

my_list = ["apple", "banana", "apple", "apple", "orange", "banana"]

my_counter = Counter(my_list)

print(my_counter["banana"])

my_list = ["apple", "banana", "apple", "apple", "orange", "banana"]
my_counter = Counter()
for i in my_list:
    my_counter[i] += 1

print(my_counter["banana"])

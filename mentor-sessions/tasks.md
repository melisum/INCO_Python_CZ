Create a function that:

- Takes the name of a CSV file as a parameter,
- Where each row is in the following format: `<last name first name>;<birthdate in YYYY-MM-DD format>;<city name>`,
- Returns the 5 most common first names of people born between 2000 and 2023,
- Writes the first names to a text file, with each name on a new line.

The expected result should be:
  Benjamin
  Emma
  Noah
  Isabella
  Ava

Create a function that reads a text file containing data from various sources and performs the following tasks using regular expressions:

1. **Matching Email Addresses:** Read the text file and extract all valid email addresses present in the file. Valid email addresses should follow the standard format (e.g., `user@example.com`).

2. **Extracting Phone Numbers:** Extract all valid phone numbers from the text file. Valid phone numbers should match common formats like `(123) 456-7890` or `123-456-7890`.

3. **Replacing Dates:** Replace all dates in the format `MM/DD/YYYY` with `YYYY-MM-DD`.

4. **Finding URLs:** Find and extract all URLs from the text file, including both HTTP and HTTPS URLs. URLs can start with `http://`, `https://`, or `www.`.

5. **Identifying IP Addresses:** Identify and extract all valid IPv4 addresses from the text file.

6. **Extracting HTML Tags:** Extract all HTML tags (e.g., `<p>`, `<a href="https://example.com">`) from the text file.

Save all results to a new .txt file with the following format:
```python
Email Addresses:
john.doe@example.com

Phone Numbers:
(123) 456-7890

Dates:
2022-01-15

URLs:
https://www.example.com

IP Addresses:
192.168.1.1

HTML Tags:
<p>
</p>
```






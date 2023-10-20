# CLI

```
pwd
```
print working directory

```
.
```
current directory

```
..
```
parent directory

```
cd my-folder
```
change directory- move to directory named my-folder

```
cd ..
```
move to parent directory- go 1 level up

```
cd <full path>
```
move to  a completely different part of my computer

```
cd -
```
this is putting you back into the last location

```
cd /
```
this will take you into your computer's root

```
cd ~
```
this will take you into your system home folder

```
ls 
```
list all the files and folders

```
ls --help
```
see the documentation for ls command

```
ls -a
```
list all the files and folders also hidden ones

```
ls -l
```
list all the files and folders with more details

```
ls -la
```
list all the files and folders also hidden ones with more details

```
mkdir my-folder
```
make directory named my-folder

```
touch text.txt
```
make new file named text.txt

```
rm text.txt
```
remove file named text.txt

```
rmdir my-folder
```
remove folder named my-folder if it is empty

```
rm -r my-folder
```
remove folder named my-folder if it has content but also if it is empty

```
cp text.txt my-folder
```
copy the file named text.txt to directory named my-folder

```
mv text.txt new-name.txt
```
rename file named text.txt to new-name.txt

```
mv text.txt my-folder
```
move the file named text.txt to directory named my-folder

```
mv text1.txt text2.txt text3.txt -t my-folder
```
move the files named text1.txt text2.txt and text3.txt to directory named my-folder

```
echo hello
```
print word hello into terminal

```
echo hello > text.txt
```
add word hello into file named text.txt

```
echo hi >> text.txt
```
add word hi into file named text.txt and not overwrite it

```
cat text.txt
```
display content of file named text.txt

```
wc text.txt
```
display number of lines number words size in bytes and name
of file named text.txt

```
wc < text.txt
```
display number of lines number words size in bytes but not name
of file named text.txt becuase with < we are redirecting the content from the file first

```
sort text.txt
```
sort content of file named text.txt alphabeticly

```
uniq text.txt
```
display content of file without duplicates but they need to bee close to each other

```
sort text.txt | uniq
```
display content of file without duplicates

```
|
```
pipe(chain) commands together

```
grep hello text.txt
```
search in the file for the word hello and display all lines that content the word hello

```
for file in *.txt; do
    echo "$file"
done
```
list all files in the directory with a ".txt" extension

```
for file in i*; do
    echo "$file"
done
```
list all files in the directory that start with the letter "i"

```
read -p "Enter a string: " user_string
read -p "Enter a number: " user_number
```
prompt the user for input

```
if [ ${#user_string} -gt 10 ]; then
    echo "The string is longer than 10 characters."
else
    echo "The string is not longer than 10 characters."
fi
```
check if the length of the user-provided string is greater than 10 characters

```
if [ $user_number -ge 100 ]; then
    echo "The number is greater than or equal to 100."
else
    echo "The number is less than 100."
fi
```
check if the user-provided number is greater than or equal to 100

```
word_to_count="cat"
file="animals.txt"

count=$(grep -o -i "$word_to_count" "$file" | wc -l)
echo "Occurrences of '$word_to_count' in '$file': $count"
```
print occurences of word cat in file animals.txt

```
fruits=("apple" "banana" "cherry")

for fruit in "${fruits[@]}"; do
    echo "I like $fruit"
done
```
print fruits

```
command_succeeds() {
    exit_code=$((RANDOM % 4)) 
    return $exit_code
}
```
define function command_succeeds, return $exit_code with generated random number between 0 and 3 

```
retries=0

while true; do
    if command_succeeds; then
        echo "Command succeeded on attempt $retries"
        break
    else
        echo "Command failed on attempt $retries"
        retries=$((retries + 1))
        if [ $retries -ge 5 ]; then
            echo "Reached maximum number of retries."
            break
        fi
        sleep $((2**retries)) 
    fi
done
```
- create while loop
- if command_succeeds returns 0 (indicating success), it executes the code within the then block
- if command_succeeds returns a non-zero value (indicating failure), it executes the code within the else block.
- sleep command pauses the script for a duration specified in seconds














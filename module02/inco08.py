import sys
import os
import subprocess

"""a set of functions, first of which calculates the area of a arectangle"""
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("Area: " + str(area))

home = os.environ.get("HOME")
print("HOME: ", home)

user1 = os.environ.get("USER")
print("User1: ", user1)

os.environ["NEW_USER"] = "Samuel"
user2 = os.environ.get("NEW_USER")
print("User2: ", user2)

if len(sys.argv) != 2:
    print("Usage: python inco08.py action")
    sys.exit(1)

action = sys.argv[1]

if action == "calculate":
    result = 8 * 4
    print(result)
    sys.exit(0)
elif action == "exit":
    print("Exiting program")
    sys.exit(0)
else:
    print("Invalid action.")
    sys.exit(1)

gitbash = "C:\\Program Files\\Git\\bin\\bash.exe"
#gitbash = os.environ.get("GITBASH")
try:
    completed_process = subprocess.run([gitbash, "-c", "ls"], capture_output=True, text=True, shell=True, check=True)
    #completed_process = subprocess.run(["dir"], capture_output=True, text=True, shell=True, check=True)
    output = completed_process.stdout
    print(output)
    exit_code = completed_process.returncode

    if exit_code == 0:
        print("Success")
    else:
        print("Fail ", exit_code)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")









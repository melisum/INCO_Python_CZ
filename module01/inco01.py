import random

print(10 % 6) #zvyšok po delení
print(10 * 5 + 1) #najskôr vynásobí potom pripočíta
print(10 * (5 + 1)) #najskôr pripočíta potom vynásobí

integer = 5
float = 1.2

print(10 // 6) #výsledok integer
print(10 / 6) #výsledok float

# Reading inputs
name = input("Enter your name: ")
print("Hello, " + name)

print("Enter your age:")
age = int(input())
print("Your age is: " + str(age))

print("Enter your height:")
height = float(input())
print(height)

# Random number
random_number = random.randint(0, 10)

# Possible output 0, 1, 2, 3 .... 10

# Rock, Paper, Scissors Game
player_move = input("Enter your move: ")
computer_random_number = random.randint(0,2)
if computer_random_number == 0:
    computer_move = "rock"
elif computer_random_number == 1:
    computer_move = "paper"
else:
    computer_move = "scissors"

print("Your move: ", player_move)
print("Computer move: ", computer_move)

if player_move == computer_move:
    print("It is a tie!")
elif (player_move == "rock" and computer_move == "scissors") or \
        (player_move == "paper" and computer_move == "rock") or \
        (player_move == "scissors" and computer_move == "paper"):
    print("You win!")
else:
    print("Computer wins!")



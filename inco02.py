import random

# Rock, Paper, Scissors Game with function
def play_game(player_move):
    computer_random_number = random.randint(0, 2)
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


# my_move = input("Enter your move: ")
play_game("rock")


# For loop

# for j in range(1, 16):
#     print(j, end=" ")

# Draw pyramid
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************

def draw_pyramid(line_count):
    for i in range(1, line_count + 1):
        spaces = " " * (line_count - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


# 1 3 5 7 9 11 13
# 1 2 3 4 5 6 7

draw_pyramid(7)
draw_pyramid(4)
# Draw diamond Homework
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

def draw_diamond(line_count):
    draw_pyramid(line_count)

    for i in range(line_count - 1, 0, -1):
        spaces = " " * (line_count - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

draw_diamond(8)

# Draw square
# %%%%%%%%
# %      %
# %      %
# %      %
# %      %
# %      %
# %      %
# %%%%%%%%

def draw_square(line_count):
    for i in range(line_count):
        for j in range(line_count):
           if i == 0 or i == line_count - 1 or j == 0 or j == line_count -1:
               print("%", end="")
           else:
               print(" ", end="")
        print()
draw_square(8)

# Draw square with diagonal Homework
# %%%%%%%%
# %%     %
# % %    %
# %  %   %
# %   %  %
# %    % %
# %     %%
# %%%%%%%%

def draw_square(line_count):
    for i in range(line_count):
        for j in range(line_count):
           if i == 0 or i == line_count - 1 or j == 0 or j == line_count -1 or i == j:
               print("%", end="")
           else:
               print(" ", end="")
        print()
draw_square(8)

# Guess the number

def guess_number():
    n = random.randint(1, 10)
    guess = 0
    print("Guess a number from 1 to 10:")
    while guess != n:
        guess = int(input())
        if guess > n :
            print("Try guessing a smaller number.")
        elif guess < n:
            print("Try guessing a larger number.")
        else:
            print("Cg! You win!")

guess_number()

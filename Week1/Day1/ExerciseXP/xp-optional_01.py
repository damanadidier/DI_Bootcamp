# Exercise 1: What is the Season?


# 1. Ask the user to input a month (1 to 12).
# 2. Display the season of the month received:
# - Spring runs from March (3) to May (5)
# - Summer runs from June (6) to August (8)
# - Autumn runs from September (9) to November (11)
# - Winter runs from December (12) to February (2)

month = int(input("Enter a month (1-12): "))
if month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer") 
elif month in [9, 10, 11]:
    print("Autumn")
elif month in [12, 1, 2]:
    print("Winter")
else:
    print("Invalid month. Please enter a number between 1 and 12.")

# Exercise 2: For Loop


# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercise 3: While Loop


# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.
my_name = "Didier"
while True:
    user_name = input("Please enter your name: ")
    if user_name == my_name:
        print("That's my name! Stopping the loop.")
        break

#  Exercise 4: Check the index


# Using this variable:

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.

# Example: if input is Cortana we should be printing the index 1
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Please enter your name: ")
if user_name in names:
    index = names.index(user_name)
    print(f"{user_name} is in the list at index {index}.")
else:
    print(f"{user_name} is not in the list.")

# Exercise 5: Greatest Number


# Ask the user for 3 numbers and print the greatest number.

# Test Data:

# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87

# The greatest number is: 87
num1 = float(input("Input the 1st number: "))
num2 = float(input("Input the 2nd number: "))
num3 = float(input("Input the 3rd number: "))
greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")

# Exercise 6: Random number


# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says “Winner”.
# If the user guesses the wrong number print a message that says “Better luck next time.”
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop, tally up and display total games won and lost.

import random

games_won = 0
games_lost = 0
while True:
    user_input = input("Guess a number from 1 to 9 (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    if not user_input.isdigit() or not (1 <= int(user_input) <= 9):
        print("Invalid input. Please enter a number from 1 to 9.")
        continue
    user_guess = int(user_input)
    random_number = random.randint(1, 9)
    if user_guess == random_number:
        print("Winner!")
        games_won += 1
    else:
        print(f"Better luck next time. The correct number was {random_number}.")
        games_lost += 1
print(f"Total games won: {games_won}")
print(f"Total games lost: {games_lost}")

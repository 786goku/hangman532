
import random
favorite_fruits = ["Apple", "Banana", "Orange", "Strawberry", "Mango"]
word_list = favorite_fruits
word = random.choice(word_list)
print(word)
favorite_fruits = ["Apple", "Banana", "Orange", "Strawberry", "Mango"]
word_list = favorite_fruits
print(word_list)
guess = input("Enter a single letter: ")
# Note: The input function returns a string, so the user's input is stored as a string in the variable 'guess'.
guess = input("Enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

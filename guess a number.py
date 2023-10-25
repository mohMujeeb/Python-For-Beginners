#Write a Python program to guess a number between 1 and 9.
import random as rn

target_number , guess_number = rn.randint(1, 10), 0

while target_number != guess_number:
    guess_number = int(input("Guess a number between 1 and 10 until you get it right: "))
print("Well Guessed!")
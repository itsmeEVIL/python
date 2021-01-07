# program about rolling dice
# made by itsmeevil

import random

print("***Roll The Dice***")
ans = input("\nRoll dice? (Y/N): ").lower()  # lowercase the input

while ans == "y":
    if ans == "y":
        # generate random integer number between 1 and 6
        rolled = str(random.randint(1, 6))
        print(f"Dice rolled. You got {rolled}")
        ans = input("\nRoll dice again? (Y/N): ").lower()
        if ans == "n":
            print("Thanks for using!")
            break  # break from the loop
else:
    print(":/")

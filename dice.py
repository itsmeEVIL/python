# program about rolling dice
# made by itsmeevil

import random as rd

def roll():
	rolled = str(rd.randint(1, 6))
	rolled = "Dice rolled. You got " + rolled
	return rolled

print("***Roll The Dice***")
ans = input("\nRoll dice? (Y/N): ").lower()

while ans == "y":
	if ans == "y":
		print(roll())
		ans = input("\nRoll dice again? (Y/N): ")
		if ans == "n":
			print("Thanks for using!")
			quit()
else:
	print(":/")
	quit()

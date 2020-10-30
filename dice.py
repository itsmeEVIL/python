# program about rolling dice
# made by itsmeevil

# import random module
import random as rd

def roll():
	rolled = str(rd.randint(1, 6)) # generate random integer number between 1 and 6
	rolled = "Dice rolled. You got " + rolled
	return rolled # return rolled variable when function is called

print("***Roll The Dice***")
ans = input("\nRoll dice? (Y/N): ").lower() # lowercase the input

while ans == "y":
	if ans == "y":
		print(roll())
		ans = input("\nRoll dice again? (Y/N): ")
		if ans == "n":
			print("Thanks for using!")
			break # break from the loop
else:
	print(":/")
	break # break from the loop

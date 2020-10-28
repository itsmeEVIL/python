# program about number guessing
# made by itsmeevil

# import random module
import random as rd

print("***Number Guessing Game***\nYou only got 5 chances to guess the correct number")

random_number = rd.randint(1, 10) # make random integer number  between 1 and 10
user_input = int(input("\nChoose a number between 1 and 10: "))
chance = 5 

while chance <= 5:
	chance -= 1 # minus chance until answer is correct
	if user_input != random_number:
		if user_input <= random_number:
			if chance == 0:
				print("\nYou got no chance left!\nBetter luck next time!")
				break # break out from the while loop
			else:
				print("\nNumber entered is smaller than the generated number!\nYou got", chance, "chance(s) left!")
				user_input = int(input("Enter a bigger number: "))
		else:
			if chance == 0:
				print("\nYou got no chance left!\nBetter luck next time!")
				break # break out from the while loop
			else:
				print("\nNumber entered is bigger than the number generated!\nYou got", chance, "chance(s) left!")
				user_input = int(input("Enter a smaller number: "))
	else:
		print("\nGreat job!\nThe number you've guessed, ", user_input, ", is correct.")
		break # break out from the while loop

# program about number guessing
# made by itsmeevil

# import random integer from random module
from random import randint

print("***Number Guessing Game***\nYou got 5 chance(s) to guess the correct number")

rand_num = randint(1, 10) # make random integer between 1 and 10
u_inp = int(input("\nChoose a number between 1 and 10: "))
chance = 5 

while chance != 0:
	chance -= 1 # minus chance until answer is correct
	if u_inp != rand_num:
		if u_inp <= rand_num:
			print("\nNumber entered is smaller than the generated number!\nYou got", chance, "chance(s) left!")
			u_inp = int(input("Enter bigger number: "))
		else:
			print("\nNumber entered is bigger than the number generated!\nYou got", chance, "chance(s) left!")
			u_inp = int(input("Enter smaller number: "))
	else:
		print("\nThe number you've guessed, ", u_inp, ", is correct.")
		break # break out from the while loop
else:
	print("\nYou got no chance left!\nBetter luck next time!")

# program about rock, paper, scissor with computer
# made by itsmeeevil

# import random module
import random as rd

def computer():
	num = rd.randint(1, 3) # generate random integer between 1 and 3
	if num == 1:
		rock = "rock"
		return rock
	elif num == 2:
		paper = "paper"
		return paper
	elif num == 3:
		scissor = "scissor"
		return scissor

def scored():
	global u_score, c_score, rounds
	if u_score > c_score:
		print("\nFinal score: ", u_score, "-", c_score, "\nCongratulations!\nYou win againts the computer")
		again = input("\nPlay again? (Y/N): ").lower()
		if again == "y":
			u_score = 0 # reset scores
			c_score = 0 # reset scores
			rounds = 3 # reset rounds
		else:
			print("\nThanks for playing!")
			quit()
	elif u_score < c_score:
		print("\nFinal score: ", u_score, "-", c_score, "\nYou lose to the computer\nBetter luck next time")
		again = input("\nPlay again? (Y/N): ").lower()
		if again == "y":
			u_score = 0 # reset scores
			c_score = 0 # reset scores
			rounds = 3 # reset rounds
		else:
			print("\nThanks for playing!")
			quit()
	elif u_score == c_score:
		print("\nFinal score: ", u_score, "-", c_score, "\nYou are tied with the computer\nBetter luck next time")
		again = input("\nPlay again? (Y/N): ").lower()
		if again == "y":
			u_score = 0 # reset scores
			c_score = 0 # reset scores
			rounds = 3 # reset rounds
		else:
			print("\nThanks for playing!")
			quit()

print("***Rock, Paper, Scissor***\nThere are 3 rounds, the winner\nwill be dicided by the most score\nafter those 3 rounds.")

computer = computer()
rounds = 3 # rounds at start
u_score = 0 # user score
c_score = 0 # computer score

while rounds <= 3:
	rounds -= 1 # minus 1 round until round = 0
	user = input("\nChoose (rock/paper/scissor): ").lower()
	if user == "rock":
		if computer == "scissor":
			print("\nRock vs Scissor = Win")
			print("Round(s) left: ", rounds)
			u_score += 1
			if rounds == 0:
				scored()
		elif computer == "paper":
			print("\nRock vs Paper = Lose")
			print("Round(s) left: ", rounds)
			c_score += 1
			if rounds == 0:
				scored()
		elif computer == "rock":
			print("\nRock vs Rock = Tie\nAdded 1 more round")
			rounds += 1
			print("Round(s) left: ", rounds)
			if rounds == 0:
				scored()
	elif user == "paper":
		if computer == "rock":
			print("\nPaper vs Rock = Win")
			print("Round(s) left: ", rounds)
			u_score += 1
			if rounds == 0:
				scored()
		elif computer == "scissor":
			print("\nPaper vs Scissor = Lose")
			print("Round(s) left: ", rounds)
			c_score += 1
			if rounds == 0:
				scored()
		elif computer == "paper":
			print("\nPaper vs Paper = Tie\nAdded 1 more round")
			rounds += 1
			print("Round(s) left: ", rounds)
			if rounds == 0:
				scored()
	elif user == "scissor":
		if computer == "paper":
			print("\nScissor vs Paper = Win")
			print("Round(s) left: ", rounds)
			u_score += 1
			if rounds == 0:
				scored()
		elif computer == "rock":
			print("\nScissor vs Rock = Lose")
			print("Round(s) left: ", rounds)
			c_score += 1
			if rounds == 0:
				scored()
		elif computer == "scissor":
			print("\nScissor vs Scissor = Tie\nAdded 1 more round")
			rounds += 1
			print("Round(s) left: ", rounds)
			if rounds == 0:
				scored()
	else:
		print("\nCheck your spelling!")
		again = input("Try again? (Y/N): ").lower()
		if again == "y":
			u_score = 0 # reset scores
			c_score = 0 # reset scores
			rounds = 3 # reset rounds
		else:
			print("\nThanks for playing!")
			quit()

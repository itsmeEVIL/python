# program about rock, paper, scissor with computer
# made by itsmeeevil

# import random module
import random

print("***Rock, Paper, Scissor***")

u_score = 0  # user score
c_score = 0  # computer score
rounds = input("\nHow many round(s) do you want to play?: ")


def isnum(value):  # to check whether a value is an int or not
    try:
        int(value)
        return True
    except ValueError:
        return False


def try_again():
    global u_score, c_score, rounds
    again = input("\nTry again? (Y/N): ").lower()
    if again == "y":
        u_score = 0  # reset scores
        c_score = 0  # reset scores
        rounds = 0  # reset rounds
        x_rounds = input("\nHow many round(s) do you want to play?: ")
        if isnum(x_rounds) is True:
            rounds = x_rounds
            play(int(rounds))
        else:
            print("ERROR:\nPlease enter in how many round(s) do you want to play!")
            try_again()
    elif again == "n":
        print("\nThanks for playing!")
        quit()
    else:
        print("ERROR:\nPlease enter Y or N only!")
        try_again()


def play_again():
    global u_score, c_score, rounds
    again = input("\nPlay again? (Y/N): ").lower()
    if again == "y":
        u_score = 0  # reset scores
        c_score = 0  # reset scores
        rounds = 0  # reset rounds
        x_rounds = int(input("\nHow many round(s) do you want to play?: "))
        if isnum(x_rounds) is True:
            rounds = x_rounds
            play(int(rounds))
        else:
            print("ERROR:\nPlease enter in how many round(s) do you want to play!")
            try_again()
    elif again == "n":
        print("\nThanks for playing!")
        quit()
    else:
        print("ERROR:\nPlease enter Y or N only!")
        try_again()


def scored():
    global u_score, c_score, rounds
    if u_score > c_score:
        print("\nFinal score: ", u_score, "-", c_score,
              "\nCongratulations!\nYou won againts the computer")
        play_again()
    elif u_score < c_score:
        print("\nFinal score: ", u_score, "-", c_score,
              "\nYou lose to the computer\nBetter luck next time")
        play_again()
    elif u_score == c_score:
        print("\nFinal score: ", u_score, "-", c_score,
              "\nYou are tied with the computer\nBetter luck next time")
        play_again()


def play(rounds):
    global u_score, c_score
    for _ in range(rounds):
        num = random.randint(1, 3)
        if num == 1:
            computer = "rock"
        elif num == 2:
            computer = "paper"
        else:
            computer = "scissor"

        rounds -= 1  # minus 1 round until round = 0
        user = input("\nChoose (rock/paper/scissor): ").lower()

        if user == "rock":
            if computer == "paper":
                print("\nRock vs Paper = Lose")
                print("Round(s) left: ", rounds)
                c_score += 1
                if rounds == 0:
                    scored()
            elif computer == "rock":
                print("\nRock vs Rock = Tie")
                print("Round(s) left: ", rounds)
                if rounds == 0:
                    scored()
            elif computer == "scissor":
                print("\nRock vs Scissor = Win")
                print("Round(s) left: ", rounds)
                u_score += 1
                if rounds == 0:
                    scored()
        elif user == "paper":
            if computer == "paper":
                print("\nPaper vs Paper = Tie")
                print("Round(s) left: ", rounds)
                if rounds == 0:
                    scored()
            elif computer == "rock":
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
                print("\nScissor vs Scissor = Tie")
                print("Round(s) l eft: ", rounds)
                if rounds == 0:
                    scored()
        else:
            print("\nCheck your spelling!")
            try_again()


if isnum(rounds) is True:
    play(int(rounds))
else:
    print("ERROR:\nPlease enter in how many round(s) do you want to play!")
    try_again()

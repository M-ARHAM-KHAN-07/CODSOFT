import random

computerScore = 0
userScore = 0
options = ['rock', 'paper', 'scissor']
icons = {'paper': '✋', 'scissor': '✌', 'rock': '✊'}


def main():
    while True:
        user = UserChoice()
        computer = random.choice(options)
        Game(user, computer)
        if close():
            print(f"\nUser score = {userScore} VS Computer score = {computerScore}\n\n")
            if userScore > computerScore:
                print("Winner is User   ✨")
                break
            elif userScore < computerScore:
                print("Winner is Computer   🥺")
                break
            else:
                print("It's a Tie")
                break


def UserChoice():
    while True:
        choice = input("Enter rock, paper or scissor :- ").strip().lower()
        if choice in ["rock", "paper", "scissor"]:
            return choice
        else:
            print("Wrong Input")


def Game(user, computer):
    global computerScore
    global userScore
    print(f"user : {icons[user]} vs computer : {icons[computer]}")
    if user == computer:
        print("It's a Tie")
    elif user == 'rock':
        if computer == 'paper':
            print("Computer Wins")
            computerScore += 1
        else:
            print("User Wins")
            userScore += 1
    elif user == 'paper':
        if computer == 'rock':
            print("User Wins")
            userScore += 1
        else:
            print("Computer Wins")
            computerScore += 1
    elif user == 'scissor':
        if computer == 'paper':
            print("User Wins")
            userScore += 1
        else:
            print("Computer Wins")
            computerScore += 1

    print(f"User = {user}")
    print(f"Computer = {computer}")


def close():
    while True:
        try:
            out = input("Enter Y/y to Continue or N/n to Exit : ")
            if out in ['y', 'Y']:
                return False
            elif out in ['n', 'N']:
                return True
            else:
                raise ValueError
        except ValueError:
            print("Enter only Y/y or N/n")


if __name__ == "__main__":
    main()

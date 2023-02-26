import random


user_win = 0
computer_win = 0

listx = ["rock","paper","scissor"]

while(True):
    #this input ask for a input by the user.
    user_choice = str(input("Type Rock/Paper/Scissor or Q to quit")).lower()

    if user_choice == "q":
        quit()

    if user_choice not in ["rock","paper","scissor"]:
        print("not a valid input")
        continue 
    
    ran = random.randint(0, 2)
    computer_pick = listx[ran]
    print("The computer picked " + computer_pick)


    if user_choice == "rock" and computer_pick == "scissor":
        print("You Won!")
        user_win += 1
        continue

    elif user_choice == "paper" and computer_pick == "rock":
        print("You Won!")
        user_win += 1
        continue
    elif user_choice == "scissor" and computer_pick == " paper":
        print("You Won!")
        user_win += 1
        continue
    elif user_choice == computer_pick:
        print("You Tied with the Bot")
        continue
    else:
        print("You lost!")
        computer_win += 1
        continue

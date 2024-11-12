import random

comp_win = 0
user_win = 0

options = ["rock","paper","scissors"]
game_no = 0
while True:
    game_no += 1
    if game_no <= 3:
        user_input = input('type "rock","paper","scissors" or quit: ')
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        if user_input.lower() not in options:
            game_no -= 1
            continue
    else:
        break

    random_no = random.randint(0,2)
    #rock : 0, paper : 1, scissors : 2
    com_pick = options[random_no]
    print(f"computer picked {com_pick}")

    if user_input == "rock" and com_pick == "scissors":
        print("you won")
        user_win += 1
    elif user_input == "paper" and com_pick == "rock":
        print("you won")
        user_win += 1
    elif user_input == "scissors" and com_pick == "paper":
        print("you won")
        user_win += 1
    elif user_input == "rock" and com_pick == "rock":
        game_no -= 1
        pass
    elif user_input == "paper" and com_pick == "paper":
        game_no -= 1
        pass
    elif user_input == "scissors" and com_pick == "scissors":
        game_no -= 1
        pass
    else:
        print("you lost")
        comp_win += 1

if comp_win < user_win:
    print(f"you won,with a score of {user_win}")
elif comp_win > user_win:
    print(f"computer won,with a score of {comp_win}")
else:
    pass
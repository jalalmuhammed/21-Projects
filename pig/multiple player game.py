import random


#rolling the dice
def roll():
    min_value = 1
    max_value = 6
    rolls = random.randint(min_value,max_value)
    return rolls

while True:
    player_no = input("How many players are playing...: ")
    if player_no.isdigit():
        player_no = int(player_no)
        if 2 < player_no < 4:
            break
        else:
            print("player no should be between 2 to 4.")
    else:
        print("enter a valid number...")

max_score = 10
users = [0 for _ in range(player_no)]

while max(users) < max_score:
    for player_indx in range(len(users)):
        print(f"player no {player_indx + 1} turn now stareted...")
        current_score = 0
        user_limit = 0

        while user_limit < 3:

            value = input("do you want to roll..? (y/n): ")

            if value.lower() != "y" and value.lower() != "n":
                print("enter valid option")
                continue

            if value.lower() == "n":
                break

            #rolling...
            dice = roll()
            user_limit += 1
            print(f"Roll {user_limit}/3")

            if dice == 1:
                print("your roll is: 1,Turned Down.. ")
                current_score = 0
                break

            else:
                print(f"your roll is: {dice} !")
                current_score += dice

        users[player_indx] += current_score
        print(f"your total score is {users[player_indx]}")

        if user_limit >= 3:
            print(f"player no {player_indx + 1}'s  limit exceeded")


winner = (users.index(max(users)) + 1)
print(f"the winner is...\nplayer no: {winner}")
print("Thank you for the time")

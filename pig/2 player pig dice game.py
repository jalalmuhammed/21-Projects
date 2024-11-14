import random

#rolling the dice
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

#user score storing
user ={
    1 : 0,
    2 : 0
}
#to limit the playing by user
user_limit ={
    1 : 0,
    2 : 0
}



while True:
    game = input("Do you wnna play(P) or quit (Q): ").upper()
    if game != "Q" and game != "P":
        print("Select the Right Option")
        continue

    elif game == "Q":
        break

    elif game == "P":
        player = int(input("Who is Playing 1 or 2: "))
        if (player == 1 or 2) and (user_limit[player] <= 5 ) :
            user_limit[player] += 1
            score = roll()
            print(f"player {player} Scored +{score}. ")
            if score != 1:
                user[player] += score
                print(f"Your Total Score Updated to {user[player]}")
            elif score == 1:
                user[player] *= 0
                print(f"Player {player} Score Reached Zero")
        elif user_limit[player] > 5:
            print(f"Player {player} Limit Exceeded")
        else:
            print("Choose Correct Option..")

    #if user hitted the limit,game ends..
    if user_limit[1] > 5 and user_limit[2] > 5:
        break

    #whoever first hit 15, wins!
    if user[1] >= 15 or user[2] >= 15:
        break

#printing results
if user[1] > user[2]:
    print(f"Player 1 Succeeded with a Score Of {user[1]}")
elif user[2] > user[1]:
    print(f"Player 2 Succeeded with a Score Of {user[2]}")
else:
    print("Thank You")
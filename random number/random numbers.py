import random

in_no = input("enter top limit number: ")
if in_no.isdigit():
    input_no = int(in_no)
    if input_no <=0:
        print("enter a number larger than zero next time")
        quit()
else:
    print("enter a positive number next time")
    quit()
#printing a random number
random_guess = random.randint(0,input_no)
index_no = 0
#looping
while True:
    index_no += 1
    if index_no <= 5: #setting limit to the loop
        user_guess = input("guess the number: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("enter a valid number next time...")
            continue
    else:
        print("you lost the game...")
        break

    if user_guess == random_guess:
        print(f"you got it correctly! in your {index_no} guess")
        break
    elif user_guess < random_guess:
        print("guess little higher")
    elif user_guess > random_guess:
        print("guess little lower")
    else:
        pass


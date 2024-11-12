print("welcomw to the quiz")

playing = input("do you want to play the game?:  ")

if playing.lower() != "yes":
     quit()

print("ok let's start the game..")

track_index = 0
#asking questines......
answer = input("what id is yenjuly0090...? ")
if answer.lower() == "jalal":
    print("you got it correctly")
    track_index += 1
else:
    print("oops try again")

answer = input("how are you ")
if answer.lower() == "fine":
    print("you got it correctly")
    track_index += 1
else:
    print("oops try again")

answer = input("sugamalleeeee")
if answer.lower() == "athe":
    print("you got it correctly")
    track_index += 1
else:
    print("oops try again")

answer = input("say yur nameee ")
if answer.lower() == "jalal":
    print("you got it correctly")
    track_index += 1
else:
    print("oops try again")

answer = input("say placeee")
if answer.lower() == "mudikkode":
    print("you got it correctly")
    track_index += 1
else:
    print("oops try again")

print("so,the questines are over,results is...")
print(f"you got {track_index} questines correctly out of 5.")
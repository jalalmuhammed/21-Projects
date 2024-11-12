import random
import os

colour_list = ["orange","yellow","blue","green","white","red","violet" ]

score = 0
correct_order = ""

while True:
    new_colour = random.choice(colour_list)
    print(new_colour)
    correct_order += new_colour
    user_int = input("enter colour: ").lower().replace(" ","")
    os.system("cls")
    score +=1

    if user_int != correct_order:
        print(f"you lost! \nyour score {score}")
        break
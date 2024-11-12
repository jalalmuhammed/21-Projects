import random

colors_list = ["R","G","Y","W","v","B"]
tries = 10
code_length = 4

def generate_code():
    code = []

    for i in range(code_length):
        color = random.choice(colors_list)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input("enter guess: ").upper().split(" ")

        if len(guess) != code_length:
            print(f"guess must be in {code_length} numbers")
            continue
        for i in range(guess):
            if i not in colors_list:
                print(f"inavlid color {i},try again")
                break
        else:
               break
    return guess
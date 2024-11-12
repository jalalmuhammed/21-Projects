import time

def timer(num):
    num += 1
    while num != 0:
        time.sleep(3)
        num -= 1
        print(num)

user_no = int(input("enter a number: "))
timer(user_no)

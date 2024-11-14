

password = input("enter master password: ")

def add():
    acc_name = input("account name: ")
    acc_pass = input("password: ")

    with open("register.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow(f"Account Name: {acc_name},Account Password: {acc_pass}")

def view():
    with open("register.csv","r") as f:
        for row in f.readlines():
            print(row.rstrip())

while True:
    mode = input("would you like to add a new password or view existing ones [add/view] or q to quit: ").lower()
    if mode == "q":
        print("Thank you")
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("invalid mode.")
        continue
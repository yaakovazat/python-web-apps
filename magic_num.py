# Magic Number , ask user to guess one number between 0~ 10 ,if the user founds it ,win.

magic_number = 7
user_number= input("Guess a number: ")
if int(user_number) == magic_number:
    print("You win !")
else:
    print("Try again !")
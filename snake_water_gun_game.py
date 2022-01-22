import random
number = random.randint(1,3)
user =  input("choose snake(s), water(w) or gun(g): ")
if number ==1:
    computer = "s"
elif number == 2:
    computer = "w"
else:
    computer = "g"

if user == computer:
    print("this is a tie")
elif computer == "s":
    if user == "w":
        print( "you lose!")
    elif user == "g":
        print(" you won!")
elif computer == "w":
    if user == "g":
        print("you lose!")
    elif user == "s":
        print("you won!")
elif computer == "g":
    if user == "w":
        print("you won!")
    elif user  == "s":
        print("you lose!")

print(f"computer chose {computer}")
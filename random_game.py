import random
random_number = random.randint(1,100)
guess_the_random_number = ""
count_chances_taken = 0
total_chances = 10
print("you have total 5 chances to guess the random number:")

while random_number != guess_the_random_number:
    guess_the_random_number = int(input("enter the any random number between 1 to 100: "))
    count_chances_taken = count_chances_taken + 1
    if count_chances_taken == total_chances:
        print("Game over")
        break
    if guess_the_random_number  > random_number:
        print("your gussed number is greater than random number\n guess a smaller number")
    elif guess_the_random_number < random_number:
        print("your guessed number is smaller than ramdom number\n guess a greater number")
    else:
        print("congratulation! you gussed the correct number")

    print(f" total chances you took to guess the correct number is {count_chances_taken}")
with open("high_score.txt","r") as f:
    high_score = f.read()
if  high_score == '':
    with open("high_score.txt", "w") as f:
        f.write(str(count_chances_taken))
elif count_chances_taken < int(high_score):
    with open("high_score.txt","w") as f:
        f.write(str(count_chances_taken))







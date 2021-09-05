import time
from random import randint
people = int(input("How many people are there in this room? "))
people_out = 0
while people > 1:
    corner_number_called = randint(1, 4)
    print("10")
    time.sleep(1)
    print("9")
    time.sleep(1)
    print("8")
    time.sleep(1)
    print("7")
    time.sleep(1)
    print("6")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("0")
    time.sleep(2)
    print(f"Corner number {corner_number_called}!")
    for i in range(people):
        if int(input("What was your corner number? ")) == corner_number_called:
            print("You're out!")
            people_out -= 1
        else:
            print("You're safe!")
    people -= people_out
    print(f"There are {people_out} players that have been out this round.")
    print("Let's continue!")
name_of_winner = input("Hey, winner, what's your name? ")
print(f"Congratulations for winning and thanks for playing, {name_of_winner}")
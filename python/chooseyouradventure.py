name = input("What is your name?: ")

print(f"""Welcome to {name}'s Choose Your Own Adventure game! As you
follow the story you will be presented with choices that decide your
fate. Take care and choose wisely! Let's begin.""")

print("""You find yourself in a dark room with 2 doors. The first door
is red, the second is white!""")

door_choice = input("""Which door do you want to choose? red=red door or
white=white door: """)

if door_choice == "red":
    print("""Great, you walk through the red door and now you are in the future!
    You meet a scientist that gives you a mission of helping him save
    the world!""")

    choice_one = input("What do you want to do? 1=Accept or 2=Decline: ")

    if choice_one == "1":
        print("""_________________SUCCESS____________________
        You helped the scientist to save the world! In gratitude, the
        scientist builds a time machine and sends you home!""")
    else:
        print("""_________________GAME OVER_____________________
        Too bad! You declined the scientist's offer and now you are
        stuck in the future!""")
else:
    print("""Great, you walked through the white door and now you are in
    the past! You meet a princess that asks you to go on a quest.""")
    quest_choice = input("""Do you want to accept her offer and go on the
    quest, or do you want to stay where you are? 1=Accept and go on
    quest or 2=Stay: """)

    if quest_choice == "1":
        print("""The princess thanks you for accepting her offer. You
        begin the quest.""")
    else:
        print("""________________GAME OVER______________________
        Well, I guess your story ends here!""")
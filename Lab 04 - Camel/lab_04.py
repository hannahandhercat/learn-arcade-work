import random


def main():
    print("Welcome to Poor Decisions.")
    print()
    print("You have made a series of poor decisions and are in quite the predicament.")
    print("It seems you've somehow managed to make an entire village very upset.")
    print("Run away from the rioting villagers and try to survive, even though it's totally your fault.")
    print()

    thirst = 0
    tiredness = 0
    miles_traveled = 0
    villagers_distance = -20
    water_bottle = 3

    done = False
    while not done:

        print("A. Drink from your water bottle.")
        print("B. Run at full speed away from the rioting villagers.")
        print("C. Jog casually away from the rioting villagers.")
        print("D. Stop and rest.")
        print("E. Status check.")
        print("Q. Give up.")
        print()

        user_choice = input("What is your choice? ")
        if user_choice.lower() == "q":
            done = True
            print("Coward.")
            print("The villagers find you and get their revenge.")
            print("It is a gruesome sight.")
        elif user_choice.lower() == "e":
            print("Miles Traveled: ", miles_traveled)
            print("Drinks in water bottle: ", water_bottle)
            print("The villagers are", miles_traveled - villagers_distance, "miles behind you.")
            print()
        elif user_choice.lower() == "d":
            tiredness = 0
            villagers_distance = villagers_distance + random.randrange(7, 15)
            print("Now you're rested, although this doesn't really help you decision making.")
        elif user_choice.lower() == "b":
            miles_traveled = miles_traveled + random.randrange(10, 21)
            thirst = thirst + 1
            tiredness = tiredness + random.randrange(1, 4)
            villagers_distance = villagers_distance + random.randrange(7, 15)
            print("You have traveled", miles_traveled, "miles.")
        elif user_choice.lower() == "c":
            miles_traveled = miles_traveled + random.randrange(5, 13)
            thirst = thirst + 1
            tiredness = tiredness + 1
            villagers_distance = villagers_distance + random.randrange(7, 15)
        elif user_choice.lower() == "a":
            thirst = 0
            if water_bottle == "0":
                print("You are out of water.")
            else:
                water_bottle = water_bottle - 1
        if 4 < thirst < 6:
            print("You are thirsty!")
        elif thirst >= 6:
            done = True
            print("You have died of thirst.")
            print("The villagers find your dried, water deprived corpse.")
            print("The villagers laugh at you.")























main()

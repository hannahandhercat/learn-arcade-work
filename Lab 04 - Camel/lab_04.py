# Import random, which is necessary for generating random numbers.
import random


def main():
    """The main function of the game "Poor Decisions" """

    # Print the title and description of the opening scenario.
    print()
    print("Welcome to Poor Decisions.")
    print()
    print("You have made a series of poor decisions and are in quite the predicament.")
    print("It seems you've somehow managed to make an entire village very upset.")
    print("Run away from the rioting villagers and try to survive, even though it's totally your fault.")
    print()

    # Define the variables used in the code that need to be outside the loop.
    thirst = 0
    tiredness = 0
    miles_traveled = 0
    villagers_distance = -20
    water_bottle = 3

    # Begin the loop for the game.
    done = False
    while not done:

        # List the different in game options for the player.
        print("A. Drink from your water bottle.")
        print("B. Run at full speed away from the rioting villagers.")
        print("C. Jog casually away from the rioting villagers.")
        print("D. Stop and rest.")
        print("E. Status check.")
        print("Q. Give up.")
        print()

        # Ask the player for their choice.
        user_choice = input("What is your choice? ")
        print()

        # Define option "Q. Give up."
        if user_choice.lower() == "q":
            done = True
            print()
            print("Coward.")
            print("The villagers find you and get their revenge.")
            print("It is a gruesome sight.")

        # Define option "E. Status check."
        elif user_choice.lower() == "e":
            print()
            print("Total miles traveled: ", miles_traveled)
            print("Drinks in water bottle: ", water_bottle)
            print("The villagers are", miles_traveled - villagers_distance, "miles behind you.")
            print()

        # Define option "D. Stop and rest."
        elif user_choice.lower() == "d":
            tiredness = 0
            villagers_distance = villagers_distance + random.randrange(7, 15)
            print("Now you're rested.")
            print("Remember, the villagers never tire.")

        # Define option "B. Run at full speed away from the rioting villagers."
        elif user_choice.lower() == "b":
            singular_miles_traveled = random.randrange(10, 21)
            miles_traveled = miles_traveled + singular_miles_traveled
            thirst = thirst + 1
            tiredness = tiredness + random.randrange(1, 4)
            villagers_distance = villagers_distance + random.randrange(7, 15)
            print("You traveled", singular_miles_traveled, "miles.")

        # Define option "C. Jog casually away from the rioting villagers."
        elif user_choice.lower() == "c":
            singular_miles_traveled = random.randrange(5, 13)
            miles_traveled = miles_traveled + singular_miles_traveled
            thirst = thirst + 1
            tiredness = tiredness + 1
            villagers_distance = villagers_distance + random.randrange(7, 15)
            print("You traveled", singular_miles_traveled, "miles.")

        # Define option "A. Drink from your water bottle."
        elif user_choice.lower() == "a":
            villagers_distance = villagers_distance + random.randrange(7, 15)
            if water_bottle > 0:
                thirst = 0
                water_bottle = water_bottle - 1
                print("You have quenched your thirst")
                print("Remember, the villagers only thirst for revenge.")
            else:
                water_bottle = 0
                print("You are out of water.")

        # Define thirst and dying from thirst.
        if 4 < thirst < 6:
            if not done:
                print("You are thirsty!")
        elif thirst >= 6:
            if not done:
                done = True
                print("You have died of thirst.")
                print("The villagers find your dried, water deprived corpse.")
                print("The villagers laugh at you.")

        # Define tiredness and dying from exhaustion.
        if 5 < tiredness <= 8:
            if not done:
                print("You are tired, your fate is catching up to you.")
        elif tiredness > 8:
            if not done:
                done = True
                print("You have died from exhaustion.")
                print("Your fate has caught up with you.")
                print("The villagers, who pillage and disrespect your corpse, are your fate.")

        # Define the villagers distance away from you and dying from being caught by them.
        if 15 >= miles_traveled - villagers_distance > 0:
            print("The villagers are close, very close.")
        elif miles_traveled - villagers_distance <= 0:
            if not done:
                done = True
                print()
                print("The villagers have caught you.")
                print("Your fate is sealed.")
                print("Maybe in your next life you won't make such Poor Decisions.")

        # Define the amount of miles necessary to win and end the game.
        if miles_traveled >= 200:
            done = True
            print()
            print("You have successfully evaded the righteously angry villagers.")
            print("Congratulations, you've escaped the fate you deserved.")
            print("Now go on, and live a righteous life.")
            print("Or your Poor Decisions will inevitably catch up to you once again.")

        # Define the chances of finding a "Kind Villager".
        if random.randrange(21) == 15:
            if not done:
                thirst = 0
                tiredness = 0
                water_bottle = 3
                print()
                print("A kind villager has found you and taken you in for the night!")
                print("You are no longer tired or thirsty, and your water bottle is full!")
                print("Remember, they were only kind to you because they didn't recognize you.")
                print()


# Run the main function.
main()

class Room:
    """Define the class 'Room'."""
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    """Define the main function."""

    # Create an empty list for each instance of Room to go into.
    room_list = []

    # Create room 0 and add it to the previously created empty list.
    room = Room("You find yourself inside of a mysterious room, "
                "\ncompletely devoid of light save for a mysterious red glow."
                "\nThrough the gloom you can make out a door to your east.", None, None, 1, None)
    room_list.append(room)

    # Create room 01 and add it to the list.
    room = Room("You now find yourself in a very bright room."
                "\nAfter letting your eyes adjust you can see that you're in a sort of greenhouse."
                "\nThe soft scent of roses washes over you. "
                "\nThere is a door to your east, north, and west.", 8, None, 2, 0)
    room_list.append(room)

    # Create room 02 and add it to the list.
    room = Room("You find yourself in a room full of maps and aged photographs."
                "\nThere is gigantic globe slowly spinning in the center of the circular room."
                "\nYou enjoy the air of discovery and exploration. "
                "\nThere is a door to your east, north, and west.", 7, None, 3, 1)
    room_list.append(room)

    # Create room 03 and add it to the list.
    room = Room("You are now in a room where the walls are made up of aquariums brimming with sea life."
                "\nThere is a large tank in the floor in the center of the room."
                "\nA dolphin chirps at you from one of the tanks. "
                "\nYou make note of how cute it is. "
                "\nThere is a door to your east, north, and west.", 6, None, 4, 2)
    room_list.append(room)

    # Create room 04 and add it to the list.
    room = Room("You find yourself in a room full of rocks and minerals of every shape and size."
                "\nThe room is dimly lit, but every light fixture is uniquely and artistically bejeweled. "
                "\nYou enjoy the sound your shoes make against the shining floor of quartz. "
                "\nThere is a door to your north and west.", 5, None, None, 3)
    room_list.append(room)

    # Create room 05 and add it to the list.
    room = Room("You find yourself surrounded by hundreds of skeletons from forgotten and ancient beasts."
                "\nThe bones of the animals range in size from that of a rat to that of a small building."
                "\nYou make eye contact with a beast that sports particularly sharp teeth. "
                "\nThere is a door to your west and to your south.", None, 4, None, 6)
    room_list.append(room)

    # Create room 06 and add it to the list.
    room = Room("You find yourself in what seems to be an underground tunnel. "
                "\nSurrounding you are hundreds of thousands of bugs, all in individual terrariums. "
                "\nYour gaze falls to a colony of ants, apparently working very hard. "
                "\nThere is a door to your west, south, and east.", None, 3, 5, 7)
    room_list.append(room)

    # Create room 07 and add it to the list.
    room = Room("You are in a room filled to the brim with different types of technological wonders."
                "\nAll around you mysterious gadgets whirl and buzz to their own unique rhythms. "
                "\nWatching the small, floor cleaning, circular robot brings you a strange amount of joy. "
                "\nThere is a door to your west, south, and east.", None, 2, 6, 8)
    room_list.append(room)

    # Create room 08 and add it to the list.
    room = Room("You find yourself in a completely white room. "
                "\nThere is a sign at one end of the room that says, "
                "\n\"Thank you for visiting us today, feel free to explore the museum for as long as you'd like.\" "
                "\nIf you'd like to browse through our gift shop, simply type 'gift shop'. "
                "\nThanks for exploring with us and have a wonderful day!\" "
                "\nThere is a door to your south and east.", None, 1, 7, None)
    room_list.append(room)

    # Create and define the variable for the current room.
    current_room = 0

    # Create the main loop of the game.
    done = False
    while not done:
        # Print the description of the current room along with the user input prompt.
        print()
        print(room_list[current_room].description)
        print()
        user_input = input("What would you like to do? ")

        # Define the scenario the user encounters if they input 'north'.
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("It seems that no matter how many times you decide to bump into a wall, "
                      "\na door refuses to magically appear.")
            else:
                current_room = next_room

        # Define the scenario the user encounters if they input 'south'.
        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You jammed your finger into the wall "
                      "\nwhile reaching for a doorknob that wasn't there.")
            else:
                current_room = next_room

        # Define the scenario the user encounters if they input 'east'.
        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You managed to stub your toe by running into a wall.")
            else:
                current_room = next_room

        # Define the scenario the user encounters if they input 'west'.
        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You hurt your nose running into a wall.")
            else:
                current_room = next_room

        # Define the scenario the user encounters if they input 'quit'.
        elif user_input.lower() == "q" or user_input.lower() == "quit":
            done = True
            print()
            print("Thank you for exploring with us, see you next time!")

        # Define the scenario the user encounters if they decide input 'gift shop'.
        elif user_input.lower() == "gift shop":
            done = True
            print()
            print("You browse the gift shop wares for a while "
                  "\nand end up leaving with a cute but overpriced stuffed dolphin.")


# Run the main function.
main()

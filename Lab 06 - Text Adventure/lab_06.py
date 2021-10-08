class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []
    room = Room("""
    You are in a mysterious room encased in glass.
    You are facing east, toward a door that opens whenever you draw near to it.
    There is an identical door behind you, but it won't open.""", None, None, 1, None)
    room_list.append(room)
    room = Room("""
    You are facing east inside of room 01.
    There is a door in front of you and to your north and west.""", 8, None, 2, 0)
    room_list.append(room)
    room = Room("""
    You are facing east inside of room 02.
    There is a door in front of you and to your north and west.""", 7, None, 3, 1)
    room_list.append(room)
    room = Room("""
    You are facing east inside of room 03.
    There is a door in front of you and to your north and west.""", 6, None, 4, 2)
    room_list.append(room)
    room = Room("""
    You are facing east inside of room 04.
    There is a door to your north and west.""", 5, None, None, 3)
    room_list.append(room)
    room = Room("""
    You are facing west inside of room 05.
    There is a door in front of you and to your south.""", None, 4, None, 6)
    room_list.append(room)
    room = Room("""
    You are facing west inside of room 06.
    There is a door in front of you and to your south and east.""", None, 3, 5, 7)
    room_list.append(room)
    room = Room("""
    You are facing west inside of room 07.
    There is a door in front of you and to your south and east.""", None, 2, 6, 8)
    room_list.append(room)
    room = Room("""
    You are facing west inside of room 08.
    There is a door to your south and east.""", None, 1, 7, None)
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print(room_list[current_room].description)
        print()
        user_input = input("What would you like to do? ")
        if user_input.lower == "n" or user_input.lower == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You ran face first into a wall.")
            else:
                current_room = next_room


main()
def main():
    my_file = open("super_villains.txt")

    # General format for printing the file "super_villains.txt"
    """for line in my_file:
        line = line.strip()
        print(line)"""

    name_list = []

    for line in my_file:
        line = line.strip()
        name_list.append(line)

    my_file.close()

    print(name_list)
    print("There were", len(name_list), "names in the file.")

    # Linear Search
    key = "Octavia the Siren"

    current_list_position = 0
    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        current_list_position += 1

    if current_list_position < len(name_list):
        print("Found at:", current_list_position)
    else:
        print("Not found.")

    """
    How to print out just "Not Found" if something is NOT in a list.
    
    if current_list_position == len(name_list)
        print("Not Found")
    """



main()

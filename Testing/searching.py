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

# How many elements would I have to chek on average (100)
    # 100 / 2 = 50
# Worst case:
    # 100
# Best case:
    # 1
# Not in list:
    # 100

# Make it so it works for ANY number of elements
# Number of items in the list is n
# Average:
    # n / 2
# Worst case:
    # n
# Best case:
    # 1
# Not in list:
    # n

# You want to use the most efficient way to find a number between 1 - 128
    # 64 (Too high) (Half of 128)
    # 32 (Too low) (Half of 32)
    # 48 (Too high) (The average of 64 and 32)
    # 40 ...etc (The average of 32 and 48)

    """ Binary Search """
# 1 - 128
    # 7 (guesses)
# 1 - 256
    # 8
# 1 - 512
    # 9
# 1 - 4.2 billion
    # 32

# Lower and Upper bounds
    """ This way of searching is more complicated but WAY more efficient than linear search! """
    lower_bound = 0
    upper_bound = len(name_list) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2

        if name_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif name_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

        if found:
            print("Found at position:", middle_pos)
        if not found:
            print("Not found.")

# Worst case, binary search

    # 128 (items)

    # 7 (guesses or tries)

    # 2^7 = 128

    # 2^16 = 65536

    # 2^? = 1024 (You need a log base of 2 in order to calculate this.)

    # log2(1024) = 10

# Worst case, binary search in terms of "n"

    # log2(n) (Log base 2 of n)





main()

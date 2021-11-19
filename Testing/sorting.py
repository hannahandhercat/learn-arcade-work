# Sorting items

a_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
print(a_list)

# Swap the 15 and 14 values
temp = a_list[2]
a_list[2] = a_list[0]
a_list[0] = temp

print(a_list)

# Start

# 14 is the smallest, swap 14 to pos 0
# 15, 57, 14, 33, 72, 79, 26, 56, 42, 40

# 15 is the next smallest, swap 15 to pos 1
# 14, 57, 15, 33, 72, 79, 26, 56, 42, 40

# 26 is the next smallest, swap 26 with pos 2
# 14, 15, 57, 33, 72, 79, 26, 56, 42, 40

# 33 is the next smallest, swap 33 to pos 3
# 14, 15, 57, 33, 72, 79, 26, 56, 42, 40

# 40 is the next smallest, swap 33 to pos 4
# 14, 15, 57, 33, 40, 79, 26, 56, 42, 72

# This is SELECTION sort.
# I am SELECTING the smallest and swapping.


def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        # Swap
        temp_again = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp_again


a_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
selection_sort(a_list)
print(a_list)

# n = elements in a list
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5,000
# n = 1000, 1000 * 500 = 500,000
# n * (n / 2) = n^2 / 2
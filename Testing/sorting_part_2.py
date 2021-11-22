my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

# An insertion sort is twice as fast as the selection sort
# Insertion sort is best for lists that are nearly sorted!


def insertion_sort(a_list):
    """ Sort a list using the insertion sort """

    for key_pos in range(1, len(a_list)): # n = 100
        key_value = a_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (a_list[scan_pos] > key_value): # worst case n = 50, avg = 25
            a_list[scan_pos + 1] = a_list[scan_pos]
            scan_pos -= 1

        a_list[scan_pos + 1] = key_value


print(my_list)
insertion_sort(my_list)
print(my_list)

# Selection Sort: ALL CASES
# How many times do we loop a list?
# n = elements in a list
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5,000
# n = 1000, 1000 * 500 = 500,000
# n * (n / 2) = n^2 / 2

# Insertion sort: Worst Case
# How many times do we loop a list?
# n = elements in a list
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5,000
# n = 1000, 1000 * 500 = 500,000
# n * (n / 2) = n^2 / 2

# Insertion sort: Average Case
# How many times do we loop through an insertion list?
# n = elements in a list
# n = 10, 10 * 2.5 = 25
# n = 100, 100 * 2.5 = 2,500
# n = 1000, 1000 * 2.5 = 250,000
# n * (n / 4) = n^2 / 4

# Insertion sort: Best Case
# How many times do we loop through an insertion list?
# n = elements in a list
# n = 10, 10 * 1 = 10
# n = 100, 100 * 1 = 100
# n = 1000, 1000 * 1 = 1000
# n = n

""" 
Insertion is the all around better sort! 
"""
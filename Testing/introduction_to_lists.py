# =       [0, 1, 2, 3, 4, 5, 6, 7] - This is what the computer sees
my_list = [3, 8, 7, 0, 5, 5, 2, 1]

#  =        [0,         1,          2]
word_list = ["Knife", "Spoon", "Fork"]

#  =          [  0,      1  ]
listception = [[2, 3], [4, 5]]


# These print the same things!
for item in my_list:
    print(item)

for i in range(len(my_list)):
    print(my_list[i])

# a method used to add something to a list
my_list.append(100)
print(my_list)

# Creating a list via outside input
user_list = []

for i in range(5):
    user_input = int(input("Enter an integer: "))
    user_list.append(user_input)

print(user_list)

# How to get the sum of values in a list (you can also just use the "sum" command).
list_total = 0

for item in my_list:
    list_total += item

print(list_total)

# Loop through each element
for i in range(len(my_list)):
    my_list[i] *= 2

# This will print "L" because it is "0" to the computer
list_string = ["Life is pointless."]
print(list_string[0])

# String practice: print just the first three letters of the month that corresponds with their number
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
month = months[(n - 1) * 3:(n - 1) * 3 + 3]
print(month)

# Secret code time
plain_test = "This is a test. ABC abc"

for c in plain_test:
    x = ord(c)
    x += 1
    c2 = chr(x)
    print(c2, end="")

# decrypting time

encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"

for c in encrypted_text:
    x = ord(c)
    x += 1
    c2 = chr(x)
    print(c2, end="")

# Print the largest number
biggest_number = my_list[0]
for item in my_list:
    if item > biggest_number:
        biggest_number = item

print(biggest_number)

# Print only positive numbers within a list
positive_outlook_list = []
for item in my_list:
    if item > 0:
        positive_outlook_list.append(item)

print(positive_outlook_list)
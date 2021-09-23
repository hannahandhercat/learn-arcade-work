# 'for loops' -  when you know how many times to loop
# 'while loops' - loop until a condition

repetitions = int(input("How many times?"))

# Repeat print statement(s) 5 times
for i in range(5):
    print("I will not chew gum in class.")
    print("But I can drink water")

# Use a variable to decide how many loops.
for i in range(repetitions):
    print("I will not chew gum in class")

# Computers count up from 0, not 1, because they are strange.
for i in range(10):
    print(i)

# "i" stands for "increment" but you do not have to use "i".
for star_count in range(10):
    print(star_count)

# Because computer is dumb, if you want to count to ten it has to look like this.
for i in range(1, 11):
    print(i)

# Code starts at two and goes up in increments of two, ending at 10 because computer is dumb
for i in range(2, 12, 2):
    print(i)

# Count down from 10
for i in range(10, -1, -1):
    print(i)

# Nested loop, loop inside a loop, this one represents T I M E
for hour in range(1, 13):
    for minute in range(60):
        print(hour, minute)

    # Running total
total = 0
for i in range(5):
    new_number = int(input("Enter a number:"))
    total += new_number

print("the total is", total)

# Code that will print "Hello" 5 times and "there" 1 time
for i in range(5):
    print("Hello")
print("there")

# While loop - this loop will end when i is equal to 10
i = 0
while i < 10:
    print(i)
    i += 1

# while loop that starts at 10 and counts down to 0
i = 10
while i > -1:
    print(i)
    i -= 1


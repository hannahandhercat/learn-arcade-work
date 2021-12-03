import random

# Justify the numbers using an f string
for i in range(10):
    x = random.randrange(120)
    print(f"My number: {x:3}")

for i in range(10):
    x = random.randrange(10000)
    print(f"My number: {x:5}")

# Add commas to your numbers; the comma counts as a character
# So to set it back to being right justified you must raise the number of characters by 1.
for i in range(10):
    x = random.randrange(10000)
    print(f"My number: {x:6,}")

x = 5
y = 66
z = 777

# Print the variable and what it's equal to.
print(f"{x=} {y=} {z=}")


my_fruit = ["Apples","Oranges","Grapes","Pears"]
my_calories = [4, 300, 70, 30]

"""Specify which way you would like your answer to justify by putting a < or > between 
the colon and the number of characters. """
for i in range(4):
    print(f"{my_fruit[i]:7} are {my_calories[i]:3} calories.")

# How to use leading zeros: shown in the "minutes".
for hours in range(1, 13):
    for minutes in range(0, 60):
        print(f"Time {hours}:{minutes:02}")
print()

# Floating Point Numbers
x = 0.1
y = 123.456789

print(f"{x:.1}  {y:.1}")
print(f"{x:.2}  {y:.2}")
print(f"{x:.3}  {y:.3}")
print(f"{x:.4}  {y:.4}")
print(f"{x:.5}  {y:.5}")
print(f"{x:.6}  {y:.6}")

print()
print(f"{x:.1f}  {y:.1f}")
print(f"{x:.2f}  {y:.2f}")
print(f"{x:.3f}  {y:.3f}")
print(f"{x:.4f}  {y:.4f}")
print(f"{x:.5f}  {y:.5f}")
print(f"{x:.6f}  {y:.6f}")

# Printing Dollars and Cents: The WRONG way!
cost1 = 3.07
tax1 = cost1 * 0.06
total1 = cost1 + tax1

print(f"Cost:  ${cost1:5.2f}")
print(f"Tax:    {tax1:5.2f}")
print(f"-------------")
print(f"Total: ${total1:5.2f}")

cost2 = 5.07
tax2 = cost2 * 0.06
total2 = cost2 + tax2

print()
print(f"Cost:  ${cost2:5.2f}")
print(f"Tax:    {tax2:5.2f}")
print(f"-------------")
print(f"Total: ${total2:5.2f}")

print()
grand_total = total1 + total2
print(f"Grand total: ${grand_total:5.2f}")
print()

# Print formatting can hide information from you.
# Therefore, create your code like THIS!

# Print Dollars and Cents: The RIGHT way!
cost1 = 3.07
tax1 = round(cost1 * 0.06, 2)
total1 = cost1 + tax1

print(f"Cost:  ${cost1:5.2f}")
print(f"Tax:    {tax1:5.2f}")
print(f"-------------")
print(f"Total: ${total1:5.2f}")

cost2 = 5.07
tax2 = round(cost2 * 0.06, 2)
total2 = cost2 + tax2

print()
print(f"Cost:  ${cost2:5.2f}")
print(f"Tax:    {tax2:5.2f}")
print(f"-------------")
print(f"Total: ${total2:5.2f}")

print()
grand_total = total1 + total2
print(f"Grand total: ${grand_total:5.2f}")
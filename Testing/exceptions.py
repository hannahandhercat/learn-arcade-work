# Vocabulary

"""
Exception: This term could mean one of two things. First, the condition that results in abnormal program flow.
Or it could be used to refer to an object that represents the data condition.
Each exception has an object that holds information about it.

Exception handling: The process of handling an exception to normal program flow.

Catch block or exception block: Code that handles an abnormal condition is said to “catch” the exception.

Throw or raise: When an abnormal condition to the program flow has been detected,
an instance of an exception object is created. It is then “thrown” or “raised” to code that will catch it.

Unhandled exception or Uncaught exception: An exception that is thrown, but never caught.
This usually results in an error and the program ending or crashing.

Try block: A set of code that might have an exception thrown in it.
"""

# Divide by zero
try:
    x = 5 / 0
except:
    print("Error dividing by zero")

# Invalid number conversion
try:
    x = int("fred")
except:
    print("Error converting fred to a number")

# Invalid number conversion but BETTER!
number_entered = False
while not number_entered:
    number_string = input("Enter an integer: ")
    try:
        n = int(number_string)
        number_entered = True
    except:
        print("Error, invalid integer")

# Multiple errors
try:
    # Open the file
    filename = "myfile.txt"
    my_file = open(filename)

    # Read from the file and strip any trailing line feeds
    my_line = my_file.readline()
    my_line = my_line.strip()

    # Convert to a number
    my_int = int(my_line)

    # Do a calculation
    my_calculated_value = 101 / my_int

# The documentation for Python has an exceptions library: http://docs.python.org/library/exceptions.html
except FileNotFoundError:
    print(f"Could not find the file '{filename}'.")
except IOError:
    print(f"Input/Output error when accessing the file '{filename}'.")
except ValueError:
    print("Could not convert data to an integer.")
except ZeroDivisionError:
    print("Division by zero error.")
except:
    print("Unexpected error.")

"""
Show how to use exceptions to save a high score for a game.

Sample Python/Pygame Programs
Simpson College Computer Science
http://simpson.edu/computer-science/
"""


def get_high_score():
    # Default high score
    high_score = 0

    # Try to read the high score from a file (the "r" stands for "read")
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")

    return high_score


def save_high_score(new_high_score):
    try:
        # Write the file to disk (the "w" stands for "write")
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")


def main():
    """ Main program is here. """
    # Get the high score
    high_score = get_high_score()

    # Get the score from the current game
    current_score = 0
    try:
        # Ask the user for his/her score
        current_score = int(input("What is your score? "))
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")

    # See if we have a new high score
    if current_score > high_score:
        # We do! Save to disk
        print("Yea! New high score!")
        save_high_score(current_score)
    else:
        print("Better luck next time.")

# Call the main function, start up the game
if __name__ == "__main__":
    main()

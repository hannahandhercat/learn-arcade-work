class Character:
    """
    This is a video game character
    """
    # Functions are called methods when inside of classes.
    def __init__(self):
        """Create my character"""
        self.name = ""
        self.outfit = ""
        self.max_hit_points = 0
        self.current_hit_points = 0
        self.armor_amount = 0
        self.max_speed = 0


class Address:
    """ Hold all the fields for a mailing address. """
    def __init__(self):
        """ Set up the address fields. """
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""


class Dog:
    def __init__(self, name):
        """ Constructor """

        self.name = name
        print("A dog has been born!")


class Person:
    def __init__(self):

        self.name: str = "A"


mary = Person()
mary.name = 22


def main():
    # This creates the dog
    my_dog = Dog("Spot")
    print(f"The dog's name is: {my_dog.name}")


main()


# Static Variables: where the variable stays the same in all instances of a class.
class Cat:
    population = 0

    def __init__(self, name):
        self.name = name

        Cat.population += 1


def main():
    cat1 = Cat("Pat")
    cat2 = Cat("Pepper")
    cat3 = Cat("Pouncy")

    print("The cat population is:", Cat.population)


main()
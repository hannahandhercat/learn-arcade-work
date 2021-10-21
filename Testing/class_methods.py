# Dog things
class Dog:
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        if self.weight < 10:
            print("Yip says", self.name)
        else:
            print("Woof says", self.name)


def main():
    my_dog = Dog()
    my_dog.name = "Spot"
    my_dog.weight = 30
    my_dog.age = 3

    my_other_dog = Dog()
    my_other_dog.name = "Fluffy"
    my_other_dog.weight = 5
    my_other_dog.age = 3

    my_other_dog.bark()
    my_dog.bark()


main()



from abc import ABC, abstractmethod
from calendar import month


class Animal(ABC):
    @abstractmethod
    def climb(self):
        pass

# TODO: implement two classes that inherit from Animal and that adhere to the LSP.
# TODO: think about an animal which would violate the LSP if it would inherit from Animal()
# TODO: think about how you would fix this

# TODO: your classes go here

class Monkey(Animal):

    def climb(self):
        print("Monkey climbs")

class Cat(Animal):

    def climb(self):
        print("Cat climbs")

# violating:

class Elephant(Animal):

    def climb(self):
        raise NotImplemented("Elephant does not implement climb. Elephant too heaving and missing paws / hands")

def climb_something(animal: Animal):
    animal.climb()

monkey = Monkey()
cat = Cat()
elephant = Elephant()

# TODO: call climb something with your objects
climb_something(monkey)
climb_something(cat)
try:
    climb_something(elephant)
except:
    print("Elephant threw exception")


#
# Fix
#

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class CanClimb(ABC):
    @abstractmethod
    def climb(self):
        pass

class Monkey(Animal, CanClimb):

    def move(self):
        print("Monkey moves")

    def climb(self):
        print("Monkey climbs")

class Cat(Animal, CanClimb):

    def move(self):
        print("Cat moves")

    def climb(self):
        print("Cat climbs")


class Elephant(Animal):

    def move(self):
        print("Elephant moves")



def move_somewhere(animal: Animal):
    animal.move()

def climb_something(climbing_animal: CanClimb):
    climbing_animal.climb()


monkey = Monkey()
cat = Cat()
elephant = Elephant()

move_somewhere(monkey)
move_somewhere(cat)
move_somewhere(elephant)

climb_something(monkey)
climb_something(cat)
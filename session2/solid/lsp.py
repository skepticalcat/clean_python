from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def climb(self):
        pass

# TODO: implement two classes that inherit from Animal and that adhere to the LSP.
# TODO: think about an animal which would violate the LSP if it would inherit from Animal()
# TODO: think about how you would fix this (no need to write it out, but feel free to if you want)

# TODO: your classes go here


def climb_something(animal: Animal):
    animal.climb()

# TODO: call climb something with your objects
climb_something(...)
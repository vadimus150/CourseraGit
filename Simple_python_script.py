#!/usr/bin/python

class Robot:

    def __init__(self, name, classification):
        self.name = name
        self.classification = classification

    @staticmethod
    def fight():
        """Whoa some dance here"""
        return "Finally! our battle will be legendary"

    @staticmethod
    def hungry():
        """"Robot hungry? Are you sure?"""
        return "I'm hungry"


if __name__ == "__main__":
    godzilla = Robot("GODzilla", "Reptile")
    print(godzilla.fight())

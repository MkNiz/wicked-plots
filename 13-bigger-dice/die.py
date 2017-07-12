from random import randint

class Die():
    """Represents a single die"""

    def __init__(self, sides=6):
        """Initialize the die; 6-sided by default"""
        self.sides = sides

    def roll(self):
        """Return a value between 1-self.sides"""
        return randint(1, self.sides)

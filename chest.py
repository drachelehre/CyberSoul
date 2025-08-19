from parts import *
from lists import *

class Chest(Part):
    def __init__(self, condition, worth, cost, defense):
        super().__init__(condition, worth, cost)
        self.defense = defense

    def chest_adjust(self):
        if self.condition == "decayed":
            self.worth = max(25, int(self.worth * 0.25))
            self.cost = max(5, int(self.cost * 0.1))
            self.defense = max(5, int(self.cost * 0.25))

        elif self.condition == "poor":
            self.worth = max(50, int(self.worth * 0.50))
            self.cost = max(7, int(self.cost * 0.5))
            self.defense = max(10, int(self.cost * 0.5))

        elif self.condition == "subpar":
            self.worth = max(75, int(self.worth * 0.75))
            self.cost = max(12, int(self.cost * 0.75))
            self.defense = max(20, int(self.cost * 0.75))

        elif self.condition == "excellent":
            self.worth = max(400, int(self.worth * 1.25))
            self.cost = max(18, int(self.cost * 1.25))
            self.defense = max(40, int(self.cost * 1.25))

        elif self.condition == "pristine":
            self.worth = max(1000, int(self.worth * 2))
            self.cost = max(25, int(self.cost * 2))
            self.defense = max(100, int(self.cost * 2))

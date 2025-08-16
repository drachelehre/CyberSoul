from parts import *
from lists import *


class MeleeArm(Part):
    def __init__(self, condition, worth, cost, melee_attack, melee_size):
        super().__init__(condition, worth, cost)
        self.melee_attack = melee_attack
        self.melee_size = melee_size

    def melee_adjust(self):
        if self.condition == "decayed":
            self.worth = max(25, int(self.worth * 0.25))
            self.cost = max(5, int(self.cost * 0.1))
            self.melee_attack = max(5, int(self.melee_attack * 0.25))
            self.melee_size = max(20, int(self.melee_size * 0.25))

        elif self.condition == "poor":
            self.worth = max(50, int(self.worth * 0.50))
            self.cost = max(7, int(self.cost * 0.5))
            self.melee_attack = max(10, int(self.melee_attack * 0.50))
            self.melee_size = max(40, int(self.melee_size * 0.50))

        elif self.condition == "subpar":
            self.worth = max(75, int(self.worth * 0.75))
            self.cost = max(12, int(self.cost * 0.75))
            self.melee_attack = max(20, int(self.melee_attack * 0.75))
            self.melee_size = max(80, int(self.melee_size * 0.75))

        elif self.condition == "excellent":
            self.worth = max(400, int(self.worth * 1.25))
            self.cost = max(18, int(self.cost * 1.25))
            self.melee_attack = max(40, int(self.melee_attack * 1.25))
            self.melee_size = max(120, int(self.melee_size * 1.25))

        elif self.condition == "pristine":
            self.worth = max(1000, int(self.worth * 2))
            self.cost = max(25, int(self.cost * 2))
            self.melee_attack = max(100, int(self.melee_attack * 2))
            self.melee_size = max(200, int(self.melee_size * 2))

from parts import *
from lists import *


class RangedArm(Part):
    def __init__(self, condition, worth, cost, ranged_bonus, shoot_bonus):
        super().__init__(condition, worth, cost)
        self.ranged_bonus = ranged_bonus
        self.shoot_bonus = shoot_bonus

    def cost_adjust(self):
        if self.condition == "decayed":
            self.worth = max(25, int(self.worth * 0.25))
            self.cost = max(5, int(self.cost * 0.1))
            self.ranged_bonus = max(5,int(self.ranged_bonus * 0.25))
            self.shoot_bonus = max(20, int(self.shoot_bonus * 0.25))
        elif self.condition == "poor":
            self.worth = max(50, int(self.worth * 0.50))
            self.cost = max(7, int(self.cost * 0.5))
            self.ranged_bonus = max(10, int(self.ranged_bonus * 0.50))
            self.shoot_bonus = max(40, int(self.shoot_bonus * 0.50))
        elif self.condition == "subpar":
            self.worth = max(75, int(self.worth * 0.75))
            self.cost = max(12, int(self.cost * 0.75))
            self.ranged_bonus = max(20, int(self.ranged_bonus * 0.75))
            self.shoot_bonus = max(80, int(self.shoot_bonus * 0.75))
        elif self.condition == "excellent":
            self.worth = max(400, int(self.worth * 1.25))
            self.cost = max(18, int(self.cost * 1.25))
            self.ranged_bonus = max(40, int(self.ranged_bonus * 1.25))
            self.shoot_bonus = max(120, int(self.shoot_bonus * 1.25))
        elif self.condition == "pristine":
            self.worth = max(1000, int(self.worth * 2))
            self.cost = max(25, int(self.cost * 2))
            self.ranged_bonus = max(100, int(self.ranged_bonus * 2))
            self.shoot_bonus = max(200, int(self.shoot_bonus * 2))

from parts import *


class MeleeArm(Part):
    def __init__(self, condition, worth, cost, melee_bonus, melee_size):
        super().__init__(condition, worth, cost)
        self.melee_bonus = melee_bonus
        self.melee_size = melee_size

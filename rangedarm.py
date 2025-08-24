from parts import *
from lists import *


class RangedArm(Part):
    def __init__(self, condition, worth, cost, ranged_attack, shoot_range, rate, name='RangedArm'):
        super().__init__(condition, worth, cost)
        self.name = name
        self.ranged_attack = ranged_attack
        self.shoot_range = shoot_range
        self.rate = rate

    def ranged_adjust(self):
        if self.condition == "Decayed":
            self.worth = max(25, int(self.worth * 0.25))
            self.cost = max(5, int(self.cost * 0.1))
            self.ranged_attack = max(5, int(self.ranged_attack * 0.25))
            self.shoot_range = max(20, int(self.shoot_range * 0.25))
            self.rate = min(2.0, self.rate * 2)
        elif self.condition == "Poor":
            self.worth = max(50, int(self.worth * 0.50))
            self.cost = max(7, int(self.cost * 0.5))
            self.ranged_attack = max(10, int(self.ranged_attack * 0.50))
            self.shoot_range = max(40, int(self.shoot_range * 0.50))
            self.rate = min(1.75, self.rate * 1.75)
        elif self.condition == "Subpar":
            self.worth = max(75, int(self.worth * 0.75))
            self.cost = max(12, int(self.cost * 0.75))
            self.ranged_attack = max(20, int(self.ranged_attack * 0.75))
            self.shoot_range = max(80, int(self.shoot_range * 0.75))
            self.rate = min(1.5, self.rate * 1.5)
        elif self.condition == "Excellent":
            self.worth = max(400, int(self.worth * 1.25))
            self.cost = max(18, int(self.cost * 1.25))
            self.ranged_attack = max(40, int(self.ranged_attack * 1.25))
            self.shoot_range = max(120, int(self.shoot_range * 1.25))
            self.rate = min(0.50, self.rate * 0.50)
        elif self.condition == "Pristine":
            self.worth = max(1000, int(self.worth * 2))
            self.cost = max(25, int(self.cost * 2))
            self.ranged_attack = max(100, int(self.ranged_attack * 2))
            self.shoot_range = max(200, int(self.shoot_range * 2))
            self.rate = min(0.1, self.rate * 0.2)

    def to_dict(self):
        return {
            "type": "RangedArm",
            "name": self.name,
            "condition": self.condition,
            "worth": self.worth,
            "cost": self.cost,
            "ranged_attack": self.ranged_attack,
            "shoot_range": self.shoot_range,
            "rate": self.rate
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            condition=data["condition"],
            worth=data["worth"],
            cost=data["cost"],
            ranged_attack=data["ranged_attack"],
            shoot_range=data["shoot_range"],
            rate=data["rate"],
            name=data.get("name", "Ranged Arm")
        )
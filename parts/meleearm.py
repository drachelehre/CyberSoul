from entities.player import *
from .parts import *


class MeleeArm(Part):
    def __init__(self,condition, worth, cost, melee_attack, melee_size, name="MeleeArm"):
        super().__init__(condition, worth, cost)
        self.name = name
        self.melee_attack = melee_attack
        self.melee_size = melee_size

    def melee_adjust(self):
        if self.condition == "Decayed":
            self.worth = max(25, int(self.worth * 0.25))
            self.cost = max(5, int(self.cost * 0.1))
            self.melee_attack = max(5, int(self.melee_attack * 0.25))
            self.melee_size = max(10, int(self.melee_size * 0.25))

        elif self.condition == "Poor":
            self.worth = max(50, int(self.worth * 0.50))
            self.cost = max(7, int(self.cost * 0.5))
            self.melee_attack = max(10, int(self.melee_attack * 0.50))
            self.melee_size = max(15, int(self.melee_size * 0.50))

        elif self.condition == "Subpar":
            self.worth = max(75, int(self.worth * 0.75))
            self.cost = max(12, int(self.cost * 0.75))
            self.melee_attack = max(20, int(self.melee_attack * 0.75))
            self.melee_size = max(20, int(self.melee_size * 0.75))

        elif self.condition == "Excellent":
            self.worth = max(400, int(self.worth * 1.02))
            self.cost = max(18, int(self.cost * 1.1))
            self.melee_attack = max(40, int(self.melee_attack * 1.02))
            self.melee_size = max(40, int(self.melee_size * 1.02))

        elif self.condition == "Pristine":
            self.worth = max(1000, int(self.worth * 1.2))
            self.cost = max(25, int(self.cost * 1.2))
            self.melee_attack = max(100, int(self.melee_attack * 1.2))
            self.melee_size = max(50, int(self.melee_size * 1.2))

    def to_dict(self):
        return {
            "type": "MeleeArm",
            "name": self.name,
            "condition": self.condition,
            "worth": self.worth,
            "cost": self.cost,
            "melee_attack": self.melee_attack,
            "melee_size": self.melee_size
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            condition=data["condition"],
            worth=data["worth"],
            cost=data["cost"],
            melee_attack=data["melee_attack"],
            melee_size=data["melee_size"],
            name=data.get("name", "Melee Arm")
        )

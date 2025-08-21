from parts import *


class Chip(Part):
    def __init__(self, condition, worth, cost, melee_rate, regenerate, regen_rate, name="Chip"):
        super().__init__(condition, worth, cost)
        self.name = name
        self.melee_rate = melee_rate
        self.regenerate = regenerate
        self.regen_rate = regen_rate

    def legs_adjust(self):
        if self.condition == "decayed":
            self.worth = int(self.worth * 0.25)
            self.cost = int(self.cost * 0.1)
            self.melee_rate = int(self.melee_rate * 0.25)
            self.regenerate = int(self.regenerate * 0.25)
            self.regen_rate = min(5, int(self.melee_rate * 4))

        elif self.condition == "poor":
            self.worth = int(self.worth * 0.50)
            self.cost = int(self.cost * 0.5)
            self.melee_rate = int(self.melee_rate * 0.25)
            self.regenerate = int(self.regenerate * 0.25)
            self.regen_rate = min(4, int(self.melee_rate * 3))

        elif self.condition == "subpar":
            self.worth = int(self.worth * 0.75)
            self.cost = int(self.cost * 0.75)
            self.melee_rate = int(self.melee_rate * 0.25)
            self.regenerate = int(self.regenerate * 0.25)
            self.regen_rate = min(3, int(self.melee_rate * 2))

        elif self.condition == "excellent":
            self.worth = int(self.worth * 1.25)
            self.cost = int(self.cost * 1.25)
            self.melee_rate = int(self.melee_rate * 0.25)
            self.regenerate = int(self.regenerate * 0.25)
            self.regen_rate = min(1, int(self.melee_rate * 0.75))

        elif self.condition == "pristine":
            self.worth = int(self.worth * 2)
            self.cost = int(self.cost * 2)
            self.melee_rate = int(self.melee_rate * 0.25)
            self.regenerate = int(self.regenerate * 0.25)
            self.regen_rate = min(.5, int(self.melee_rate * 0.25))

    def to_dict(self):
         return {
            "type": "Chest",
            "name": self.name,
            "condition": self.condition,
            "worth": self.worth,
            "cost": self.cost,
            "melee_rate": self.melee_rate,
            "regenerate": self.regenerate,
            "regen_rate": self.regen_rate
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            condition=data["condition"],
            worth=data["worth"],
            cost=data["cost"],
            melee_rate=data["melee_rate"],
            regenerate=data["regenerate"],
            regen_rate=data["regen_rate"],
            name=data.get("name", "Chest")
        )
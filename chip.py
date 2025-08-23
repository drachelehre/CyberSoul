from parts import *


class Chip(Part):
    def __init__(self, condition, worth, cost, melee_rate, regenerate, regen_rate, name="Chip"):
        super().__init__(condition, worth, cost)
        self.name = name
        self.melee_rate = melee_rate
        self.regenerate = regenerate
        self.regen_rate = float(regen_rate)

    def chip_adjust(self):
        if self.condition == "decayed":
            self.worth = round(self.worth * 0.25, 2)
            self.cost = round(self.cost * 0.1, 2)
            self.melee_rate = round(self.melee_rate * 0.25, 2)
            self.regenerate = round(self.regenerate * 0.25, 2)
            self.regen_rate = round(min(5, self.regen_rate * 4), 2)

        elif self.condition == "poor":
            self.worth = round(self.worth * 0.50, 2)
            self.cost = round(self.cost * 0.5, 2)
            self.melee_rate = round(self.melee_rate * 0.25, 2)
            self.regenerate = round(self.regenerate * 0.25, 2)
            self.regen_rate = round(min(4, self.regen_rate * 3), 2)

        elif self.condition == "subpar":
            self.worth = round(self.worth * 0.75, 2)
            self.cost = round(self.cost * 0.75, 2)
            self.melee_rate = round(self.melee_rate * 0.25, 2)
            self.regenerate = round(self.regenerate * 0.25, 2)
            self.regen_rate = round(min(3, self.regen_rate * 2), 2)

        elif self.condition == "excellent":
            self.worth = round(self.worth * 1.25, 2)
            self.cost = round(self.cost * 1.25, 2)
            self.melee_rate = round(self.melee_rate * 0.25, 2)
            self.regenerate = round(self.regenerate * 0.25, 2)
            self.regen_rate = round(min(1, self.regen_rate * 0.75), 2)

        elif self.condition == "pristine":
            self.worth = round(self.worth * 2, 2)
            self.cost = round(self.cost * 2, 2)
            self.melee_rate = round(self.melee_rate * 0.25, 2)
            self.regenerate = round(self.regenerate * 0.25, 2)
            self.regen_rate = round(min(0.5, self.regen_rate * 0.25), 2)

    def to_dict(self):
        return {
            "type": "Chip",
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
            name=data.get("name", "Chip")
        )
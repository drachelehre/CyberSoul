from parts import *
from lists import *

class Chest(Part):
    def __init__(self, condition, worth, cost, defense, name="Chest"):
        super().__init__(condition, worth, cost)
        self.name = name
        self.defense = defense

    def chest_adjust(self):
        if self.condition == "Decayed":
            self.worth = max(25, int(self.worth * 0.25))
            self.cost = max(5, int(self.cost * 0.1))
            self.defense = max(5, int(self.defense * 0.25))

        elif self.condition == "Poor":
            self.worth = max(50, int(self.worth * 0.50))
            self.cost = max(7, int(self.cost * 0.5))
            self.defense = max(10, int(self.defense * 0.5))

        elif self.condition == "Subpar":
            self.worth = max(75, int(self.worth * 0.75))
            self.cost = max(12, int(self.cost * 0.75))
            self.defense = max(20, int(self.defense * 0.75))

        elif self.condition == "Excellent":
            self.worth = max(400, int(self.worth * 1.25))
            self.cost = max(18, int(self.cost * 1.25))
            self.defense = max(40, int(self.defense * 1.25))

        elif self.condition == "Pristine":
            self.worth = max(1000, int(self.worth * 2))
            self.cost = max(25, int(self.cost * 2))
            self.defense = max(100, int(self.defense * 2))

    def to_dict(self):
        return {
            "type": "Chest",
            "name": self.name,
            "condition": self.condition,
            "worth": self.worth,
            "cost": self.cost,
            "defense": self.defense,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            condition=data["condition"],
            worth=data["worth"],
            cost=data["cost"],
            defense=data["defense"],
            name=data.get("name", "Chest")
        )
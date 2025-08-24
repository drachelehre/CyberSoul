from parts import *


class Legs(Part):
    def __init__(self, condition, worth, cost, speed, name="Legs"):
        super().__init__(condition, worth, cost)
        self.name = name
        self.speed = speed

    def legs_adjust(self):
        if self.condition == "Decayed":
            self.worth = max(25, int(self.worth * 0.25))
            self.cost = max(5, int(self.cost * 0.1))
            self.speed = max(60, int(self.speed * 0.25))

        elif self.condition == "Poor":
            self.worth = max(50, int(self.worth * 0.50))
            self.cost = max(7, int(self.cost * 0.5))
            self.speed = max(70, int(self.speed * 0.5))

        elif self.condition == "Subpar":
            self.worth = max(75, int(self.worth * 0.75))
            self.cost = max(12, int(self.cost * 0.75))
            self.speed = max(80, int(self.speed * 0.75))

        elif self.condition == "Excellent":
            self.worth = max(400, int(self.worth * 1.25))
            self.cost = max(18, int(self.cost * 1.25))
            self.speed = max(90, int(self.speed * 1.25))

        elif self.condition == "Pristine":
            self.worth = max(1000, int(self.worth * 2))
            self.cost = max(25, int(self.cost * 2))
            self.speed = max(150, int(self.speed * 2))

    def to_dict(self):
        return {
            "type": "Legs",
            "name": self.name,
            "condition": self.condition,
            "worth": self.worth,
            "cost": self.cost,
            "speed": self.speed,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            condition=data["condition"],
            worth=data["worth"],
            cost=data["cost"],
            speed=data["speed"],
            name=data.get("name", "Legs")
        )

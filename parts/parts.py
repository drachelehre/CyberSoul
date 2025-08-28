class Part:
    """Superclass of all part subclasses"""
    def __init__(self, condition, worth, cost):
        self.condition = condition
        self.worth = worth
        self.cost = cost

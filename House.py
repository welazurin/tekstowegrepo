from Building import Building


class House(Building):
    def __init__(self):
        super().__init__("House", True)
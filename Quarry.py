from Building import Building


class Quarry(Building):
    def __init__(self):
        super().__init__("Quarry", True)

    def enter(self):
        print(self.name)
        print("Poziom: ",self.level)
        print("Aktualna Produkcja: ", self.production)
        print("Koszt budowy: ", self.cost)
        print("Czas budowy: ", self.time[0])

        print("Informacje o budynku")
        print("poziom, koszt drewna, kamienia, zlota, czas budowy, czas rozbiorki, produkcja")
        self.show_info()

    def show_info(self):
        with open("files/Gold_Mine.txt") as file:
            print(file.read())
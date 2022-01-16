from TownHall import TownHall
from Barracks import Barracks
from Academy import Academy
from GoldMine import GoldMine
from House import House
from Quarry import Quarry
from Wood_Cutter import WoodCutter


class City():
    def __init__(self):
        self.buildings = []
        town_hall = TownHall()
        barracks = Barracks()
        academy = Academy()
        gold_mine = GoldMine()
        house = House()
        quarry = Quarry()
        wood_cutter = WoodCutter()
        self.buildings.append(town_hall)
        self.buildings.append(barracks)
        self.buildings.append(academy)
        self.buildings.append(house)
        self.buildings.append(gold_mine)
        self.buildings.append(wood_cutter)
        self.buildings.append(quarry)

    def print_buildings(self):
        for i in self.buildings:
            i.print_name()

    def build(self):
        self.print_buildings()
        x = int(input("wybierz budynek"))
        self.buildings[x].build()

    def destroy(self):
        self.print_buildings()
        x = int(input("wybierz budynek"))
        self.buildings[x].destroy()

    def enter(self):
        self.print_buildings()
        x = int(input("wybierz budynek"))
        self.buildings[x].enter()

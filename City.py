from TownHall import TownHall
from Barracks import Barracks
from Academy import Academy
from GoldMine import GoldMine
from House import House
from Quarry import Quarry
from Wood_Cutter import WoodCutter
import os


class City:
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

        self.wood = 90
        self.stone = 90
        self.gold = 90
        self.people = 300
        self.in_build = []
        self.in_destroy = []
        self.tests = []
        self.done_test = []
        with open("files/Tests.txt") as file:
            test = file.read()
            lines = test.split("\n")
            for i in lines:
                if i == '':
                    pass
                else:
                    self.tests.append(i.split(" "))
        self.to_test = self.tests

    def building(self):
        while True:
            print("1 - Jesli chcesz zobaczyc informacje o budynku\n"
                  "2 - Jesli chcesz ulepszyc budynek"
                  "0 - wyjdz")
            y = int(input())
            if y == 1:
                while True:
                    for i in range(len(self.buildings)):
                        print(i+1, end=" ")
                        self.buildings[i].print_name()
                    x = int(input("wybierz budynek aby wyswielic informacje o budynku 0 - aby wyjsc"))
                    if x == 0:
                        break
                    else:
                        self.buildings[x-1].enter()
                        y = input("wpisz cokolwiek aby kontynnuowac") #TODO to rzeba zutomatyzowac tzn napisac funkcje
                        os.system('cls')
            elif y == 2:
                for i in range(len(self.buildings)):
                    print(i + 1, end=" ")
                    self.buildings[i].print_name()
                x = int(input("wybierz budynek do ulepszenia 0 - aby wyjsc"))
                if x == 0:
                    pass
                else:
                    if self.wood >= self.buildings[x].cost[0] and self.stone >= self.buildings[x].cost[1] and self.gold >= self.buildings[x].cost[2]:
                        self.wood = self.wood-self.buildings[x].cost[0]
                        self.stone = self.stone - self.buildings[x].cost[1]
                        self.gold = self.gold - self.buildings[x].cost[2]
                        temp = [x, self.buildings[x].time[0]]
                        self.in_build.append(temp)
            elif y == 3:
                for i in range(len(self.buildings)):
                    print(i + 1, end=" ")
                    self.buildings[i].print_name()
                x = int(input("wybierz budynek do ulepszenia 0 - aby wyjsc"))
                if x == 0:
                    pass
                else:
                    self.wood = self.wood+(self.buildings[x].cost[0]/2)
                    self.stone = self.stone + (self.buildings[x].cost[1]/2)
                    self.gold = self.gold + (self.buildings[x].cost[2]/2)
                    temp = [x, self.buildings[x].time[1]]
                    self.in_destroy.append(temp)
            elif y == 0:
                break

    def test(self):
        while True:
            print("1 - ukonczone badania")
            print("2 - nieukonczone badania")
            x = int(input())
            if x == 0:
                break
            elif x == 1: # ukonczone badania
                while True:
                    for i in range(len(self.done_test)):
                        print(i+1, self.done_test[i][0])
                    print("0 - wyjdz")
                    y = int(input())
                    if y == 0:
                        break
                    else:
                        print(self.done_test[y-1])
            elif x == 2:
                while True:
                    for i in range(len(self.to_test)):
                        print(i+1, self.to_test[i][0])
                    y = int(input())
                    if y == 0:
                        break
                    else:
                        print(self.to_test[y])
                        print("Czy na pewno chcesz zbadac ? T/N")
                        z = input()
                        if z == 'T' or z == 't':
                            if self.wood >= int(self.to_test[y][1]) and self.stone >= int(self.to_test[y][2]) and self.gold >= int(self.to_test[y][3]):
                                self.wood = self.wood - int(self.to_test[y][1])
                                self.stone = self.stone - int(self.to_test[y][2])
                                self.gold = self.gold - int(self.to_test[y][3])
                                self.done_test.append(self.to_test[y])
                                del self.to_test[y]
                            else:
                                print("nie masz hajsu")
                        else:
                            pass

    def enter(self):
        print("0 - koniec tury"
              "1 - zarzadzanie budynkami"
              "2 - zarzadzanie jednostkami"
              "3 - zarzadanie badaniami")
        x = int(input())
        if x == 0:
            # koniec tury
            pass
        elif x == 1:
            self.building()
        elif x == 2:
            pass #TODO jednostki
        elif x == 3:
            self.test()
''
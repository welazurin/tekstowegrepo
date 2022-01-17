import math
from abc import abstractmethod


class Building:
    def __init__(self, name, production):       #CONSTRUCTOR
        self.file_name = "files/" + name + ".txt"
        self.cost = []
        self.time = []
        with open(self.file_name, "r") as file:
            line = file.readline()
            g = line.strip('\n')
            w = g.split(sep=" ")
            self.level = int(w[0])
            for i in range(3):
                self.cost.append(int(w[1+i]))
            for i in range(2):
                self.time.append(int(w[4+i]))
        if production:
            self.production = int(w[6])
        else:
            self.production = -1
        self.name = name

    def build(self):
        with open(self.file_name, "r") as file:
            self.level = self.level+1
            while True:
                line = file.readline()
                g = line.strip('\n')
                w = g.split(sep=",")
                if int(w[0]) == self.level:
                    for i in range(3):
                        self.cost[i] = (int(w[i+1]))
                    for i in range(2):
                        self.time[i] = (int(w[i+4]))
                    if self.production != -1:
                        self.production = int(w[6])
                    break

    def destroy(self):
        with open(self.file_name, "r") as file:
            self.level = self.level-1
            while True:
                line = file.readline()
                g = line.strip('\n')
                w = g.split(sep=" ")
                if int(w[0]) == self.level:
                    for i in range(3):
                        self.cost[i] = (int(w[i+1]))
                    for i in range(2):
                        self.time[i] = (int(w[i+4]))
                    if self.production != -1:
                        self.production = int(w[6])
                    break

    def info(self):
        print(self.name)
        print(self.level)
        print(self.cost[0])
        print(self.cost[1])
        print(self.cost[2])
        print(self.time[0])
        print(self.time[1])

    def print_name(self):
        print(self.name, self.level)

    @abstractmethod
    def enter(self):
        pass


from Building import Building


class Academy(Building):
    def __init__(self):
        super().__init__("Academy", False)
        self.tests = []


    def enter(self):
        pass

    def showTests(self):
        with open("files/Tests.txt", "r") as file:
            list = file.read()
            line = list.split("\n")
            for i in line:
                if i == '':
                    pass
                else:
                    self.tests.append(i.split(" "))
        print(self.tests)

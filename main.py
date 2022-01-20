from City import City

if __name__ == '__main__':
    c = City()
    while True:
        x = int(input("meny"))
        if x == 0:
            break
        else:
            c.test()

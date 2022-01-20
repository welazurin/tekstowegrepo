# tekstowegrepo

pliki budynków np
Town_hall.txt działa tak
level, koszt drewna, koszt kamienia, koszt złota, czas ulepszania, czas rozbiorki
0,100,100,100,2,1
gdy dochodzi jakas "produkcja" czyli budynki domek, drwal, kamieniolom i kopalnia zlota na koncu maja jeszcze wartosc okreslającą ile produkują czyli
0,100,100,100,2,1,100 oznacza ze co ture dostajemy 100 drewna w przypadku drwala



# budynki bez entry()
wszystkie klasy dziedziczą po klasie building, w ktorej jest ulepszanie niszczenie info o budynku, oraz @abstractmethod entry() do napisania :D

# Entry() gotowe Dodanie City ogarniecie budowy
Wszystkie budynki maja funkcje entry() ktora wypisuje wszystkie mozliwe poziomy budynkow koszt i produkcje
klasa City zawiera informacje o surowacach badaniach jednostkach, w jej interfejsie bedzie rekrutowanie, budowanie i badanie
funkcja city.building - wyswietla informacje o budynku, ulepsza je oraz burzy

# badania zrobione
W klasie City dodana opcja badania. city.test()

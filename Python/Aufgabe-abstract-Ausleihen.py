from abc import ABC, abstractmethod
from typing import List


# --------------------------------------------------
# Interfaces
# --------------------------------------------------

class Ausleihbar(ABC):
    @abstractmethod
    def ausleihen(self):
        pass


class Aufladbar(ABC):
    @abstractmethod
    def aufladen(self):
        pass


# --------------------------------------------------
# Oberer Teil des UML-Diagramms
# Tablet + Buch implementieren Ausleihbar
# --------------------------------------------------

class Tablet(Ausleihbar):
    def __init__(self, pLZustand: int, pApps: List[str]):
        self.ladezustandInProzent = pLZustand
        self.installierteApps = pApps

    def ausleihen(self):
        return f"Tablet wird ausgeliehen. Ladezustand: {self.ladezustandInProzent}%."


class Buch(Ausleihbar):
    def __init__(self, pT: str, pA: str, pV: str, pF: str, pP: float):
        self.titel = pT
        self.autor = pA
        self.verlag = pV
        self.fach = pF
        self.preis = pP

    def ausleihen(self):
        return f"Buch '{self.titel}' von {self.autor} wird ausgeliehen."


# --------------------------------------------------
# Unterer Teil des UML-Diagramms
# Medium als Oberklasse, Handy + Tablet2 darunter
# --------------------------------------------------

class Medium(ABC):
    def __init__(self, name: str):
        self.name = name


class Handy(Medium, Aufladbar):
    def __init__(self, name: str, ladezustand: int):
        super().__init__(name)
        self.ladezustand = ladezustand

    def aufladen(self):
        self.ladezustand = 100
        return f"Handy '{self.name}' wurde aufgeladen."


class Tablet2(Medium, Ausleihbar, Aufladbar):
    def __init__(self, name: str, ladezustand: int):
        super().__init__(name)
        self.ladezustand = ladezustand

    def ausleihen(self):
        return f"Tablet '{self.name}' wird ausgeliehen."

    def aufladen(self):
        self.ladezustand = 100
        return f"Tablet '{self.name}' wurde aufgeladen."


# --------------------------------------------------
# Beispielprogramm zum Testen
# --------------------------------------------------

if __name__ == "__main__":
    # Oberes Tablet
    t1 = Tablet(80, ["YouTube", "Mail"])
    print(t1.ausleihen())

    # Buch
    b = Buch("Python 101", "Müller", "Tech-Verlag", "Informatik", 29.99)
    print(b.ausleihen())

    # Handy
    h = Handy("Samsung S20", 20)
    print(h.aufladen())

    # Tablet aus dem unteren Diagramm
    t2 = Tablet2("iPad", 50)
    print(t2.ausleihen())
    print(t2.aufladen())

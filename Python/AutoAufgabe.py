class Auto:
    __anzahl_autos = 0  # Privates Klassenattribut für die Anzahl der Autos
    __baujahr_max = 2025  # Privates Klassenattribut für das maximal erlaubte Baujahr

    def __init__(self, marke, baujahr):
        if baujahr > Auto.__baujahr_max:
            raise ValueError(f"Das Baujahr darf nicht größer als {Auto.__baujahr_max} sein.")
        self.marke = marke
        self.baujahr = baujahr
        Auto.__anzahl_autos += 1  # Erhöht die Anzahl der Autos, wenn ein neues Auto erstellt wird

    @classmethod
    def get_anzahl_autos(cls):
        return cls.__anzahl_autos

    @classmethod
    def set_baujahr_max(cls, baujahr):
        if baujahr < 1900:
            raise ValueError("Das Baujahr darf nicht kleiner als 1900 sein.")
        cls.__baujahr_max = baujahr

    @classmethod
    def get_baujahr_max(cls):
        return cls.__baujahr_max

    @classmethod
    def von_string(cls, string):
        # Hier wird die Eingabe erwartet im Format "Marke;Baujahr"
        teile = string.split(";")
        if len(teile) != 2:
            raise ValueError("Die Eingabe muss im Format 'Marke;Baujahr' sein.")
        marke = teile[0].strip()
        try:
            baujahr = int(teile[1].strip())
        except ValueError:
            raise ValueError("Das Baujahr muss eine Zahl sein.")
        return cls(marke, baujahr)


# Testcode

# Setzen des maximalen Baujahres
Auto.set_baujahr_max(2023)

# Erzeugen eines Autos über den Konstruktor
auto1 = Auto("BMW", 2022)
print(f"Auto 1: Marke={auto1.marke}, Baujahr={auto1.baujahr}")

# Erzeugen eines Autos aus einem String
auto2 = Auto.von_string("Audi;2020")
print(f"Auto 2: Marke={auto2.marke}, Baujahr={auto2.baujahr}")

# Zugriff auf die Anzahl der Autos
print(f"Anzahl der Autos: {Auto.get_anzahl_autos()}")

# Test, falls das Baujahr zu groß ist
try:
    auto3 = Auto("Mercedes", 2024)  # Sollte einen Fehler werfen
except ValueError as e:
    print(e)

# Test, falls der String das falsche Format hat
try:
    auto4 = Auto.von_string("Mercedes-2023")  # Sollte einen Fehler werfen
except ValueError as e:
    print(e)

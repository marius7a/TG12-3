class Auto:
    def __init__(self, marke="Unbekannt", modell="Standard", baujahr=2000, kilometerstand=0):
        self.__marke = marke
        self.__modell = modell
        self.set_baujahr(baujahr)
        self.set_kilometerstand(kilometerstand)

  

    def set_baujahr(self, baujahr):
        if isinstance(baujahr, int) and 1886 <= baujahr <= 2025:
            self.__baujahr = baujahr
        else:
            raise ValueError("Ungültiges Baujahr: Muss zwischen 1886 und 2025 liegen.")

    def set_kilometerstand(self, kilometerstand):
        if isinstance(kilometerstand, (int, float)) and kilometerstand >= 0:
            self.__kilometerstand = kilometerstand
        else:
            raise ValueError("Kilometerstand muss eine nicht-negative Zahl sein.")

    # __str__ Methode zur Ausgabe
    def __str__(self):
        return f"{self.__marke} {self.__modell} (Baujahr: {self.__baujahr}, Kilometerstand: {self.__kilometerstand} km)"




# Erstellen eines Autos mit Default-Werten
auto1 = Auto()
print(auto1)

# Erstellen eines Autos mit eigenen Werten
auto2 = Auto("BMW", "3er", 2018, 55000)
print(auto2)

# Setzen neuer Werte
auto2.set_kilometerstand(60000)
auto2.set_baujahr(2020)
print(auto2)

# Ungültige Werte testen (lösen Fehler aus)
try:
    auto2.set_baujahr(1700)
except ValueError as e:
    print("Fehler:", e)

try:
    auto2.set_kilometerstand(-100)
except ValueError as e:
    print("Fehler:", e)

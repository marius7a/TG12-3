class Klasse:
    # Klassenattribut (unterstrichen im UML)
    klassen_attribut = 0  # <— wird von allen Instanzen geteilt

    # Konstruktoren
    def __init__(self, p_parameter=None):
        
        # -privatesAttribut:Typ
        self.__privates_attribut = 0

        # #geschütztesAttribut:Typ
        self._geschuetztes_attribut = "intern"

        # +öffentlichesAttribut:Typ
        self.oeffentliches_attribut = 0.0

        # -attributMitZusicherung:Typ {Zusicherung}
        #  Zusicherung: > 0
        self.__attribut_mit_zusicherung = 1

        # -attributMitAnfangswert:Typ = Anfangswert
        self.attribut_mit_anfangswert = True

        # -attributKollektion:Typ[anzElemente]
        self.attribut_kollektion =  []

        # TODO Falls der optionale Konstruktor-Parameter benutzt wird,
        # setzen wir ihn als Startwert
        if p_parameter !=  None:
            self.__set_zusicherungswert(p_parameter)

        # Beispiel: Zähler hochzählen (zeigt Klassenattribut-Nutzung)
        Klasse.klassen_attribut += 1

    # ---------------- Sichtbarkeiten / Operationen ----------------
    def __private_operation(self):
        # nur intern nutzbar
        self.__privates_attribut += 1

    def _geschuetzte_operation(self) -> str:
        # Konvention: nur innerhalb der Klasse/Unterklassen verwenden
        # TODO alle Buchstaben in Grossbuchstaben umwandeln
        return self._geschuetztes_attribut.upper()
                    
    def oeffentliche_operation(self):
        # darf von außen aufgerufen werden
        # TODO private Operation aufrufen
        self.__private_operation() 
        # TODO geschützte Operation aufrufen
        self._geschuetzte_operation()

    def operation1(self, p_parameter):
        # TODO Liste genau p_parameter-mal mit 0 füllen
        self.attribut_kollektion = [0] * p_parameter

    def operation2(self):
        # gibt zusammengefasste Info über Attribut zurück
        return (f"privat={self.__privates_attribut}, "
                f"privat mit Zusicherung={self.attribut_mit_zusicherung}, "
                f"geschuetzt='{self._geschuetztes_attribut}', "
                f"oeffentlich={self.oeffentliches_attribut}, "
                f"liste_len={len(self.attribut_kollektion)}")

    @classmethod
    def klassen_operation(cls):
        return cls.klassen_attribut

    def __set_zusicherungswert(self, wert):
        # (für die Zusicherung & read-only)
        if wert <= 0:
            raise ValueError("Zusicherungswert muss > 0 sein")
        self.__attribut_mit_zusicherung = wert

    def __get_zusicherungswert(self):
        return self.__attribut_mit_zusicherung
    
    # TODO attribut_mit_zusicherung definieren
    attribut_mit_zusicherung = property(__get_zusicherungswert,__set_zusicherungswert)

    # Standard-Konstruktor
x = Klasse()
x.oeffentliche_operation()
x.operation1(3)
print(x.operation2())
print("Klassenzähler:", Klasse.klassen_operation())

# Konstruktor mit Parameter
y = Klasse(5)
print("Zusicherung y:", y.attribut_mit_zusicherung)

# Fehlerbeispiel (Zusicherung verletzt):
try:
    y.attribut_mit_zusicherung = 0       # darf nicht
except ValueError as e:
    print("Fehler:", e)
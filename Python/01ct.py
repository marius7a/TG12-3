from typing import List

class Klasse:
    # Klassenattribut (unterstrichen im UML)
    klassen_attribut: int = 0  # <— wird von allen Instanzen geteilt

    # Konstruktoren
    def __init__(self, p_parameter: int | None = None):
        
        # -privatesAttribut:Typ
        self.__privates_attribut: int = 0

        # #geschütztesAttribut:Typ
        self._geschuetztes_attribut: str = "intern"

        # +öffentlichesAttribut:Typ
        self.oeffentliches_attribut: float = 0.0

        # -attributMitZusicherung:Typ {Zusicherung}
        #  Zusicherung: > 0
        self.__attribut_mit_zusicherung: int = 1

        # -attributMitAnfangswert:Typ = Anfangswert
        self.attribut_mit_anfangswert: bool = True

        # -attributKollektion:Typ[anzElemente]
        self.attribut_kollektion: List[int] = []

        # Falls der optionale Konstruktor-Parameter benutzt wird,
        # setzen wir ihn sinnvoll als Startwert (z. B. für die Zusicherung):
        if p_parameter is not None:
            self.setze_zusicherungswert(p_parameter)

        # Beispiel: Zähler hochzählen (zeigt Klassenattribut-Nutzung)
        Klasse.klassen_attribut += 1

    # ---------------- Sichtbarkeiten / Operationen ----------------
    def __private_operation(self) -> None:
        # nur intern nutzbar
        self.__privates_attribut += 1

    def _geschuetzte_operation(self) -> None:
        # Konvention: nur innerhalb der Klasse/Unterklassen verwenden
        self._geschuetztes_attribut = self._geschuetztes_attribut.upper()

    def oeffentliche_operation(self) -> None:
        # darf von außen aufgerufen werden
        self.__private_operation()
        self._geschuetzte_operation()

    def operation1(self, p_parameter: int) -> None:
        # nutzen wir, um die Liste genau p_parameter-mal mit 0 zu füllen
        if p_parameter < 0:
            raise ValueError("p_parameter muss >= 0 sein")
        self.attribut_kollektion = [0] * p_parameter

    def operation2(self) -> str:
        # geben wir irgendeine zusammengefasste Info zurück
        return (f"privat={self.__privates_attribut}, "
                f"geschuetzt='{self._geschuetztes_attribut}', "
                f"oeffentlich={self.oeffentliches_attribut}, "
                f"liste_len={len(self.attribut_kollektion)}")

    @classmethod
    def klassen_operation(cls) -> int:
        return cls.klassen_attribut

    # (für die Zusicherung & read-only)
    def setze_zusicherungswert(self, wert: int) -> None:
        if wert <= 0:
            raise ValueError("Zusicherungswert muss > 0 sein")
        self.__attribut_mit_zusicherung = wert

    @property
    def zusicherungswert(self) -> int:
        """read-only Zugriff, zeigt 'abgeleitet/read-only' Idee"""
        return self.__attribut_mit_zusicherung
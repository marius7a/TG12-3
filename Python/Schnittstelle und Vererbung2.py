from typing import Protocol
 
class Lenkbar(Protocol):
    def lenke(self, winkel: int) -> None: ...
 
 
class Auto:
    def __init__(self, marke: str, modell: str):
        self.marke = marke
        self.modell = modell
 
    def lenke(self, winkel: int) -> None:
        print(f"{self.marke} {self.modell} lenkt um {winkel}°")
 
 
class Fahrrad:
    def lenke(self, winkel: int) -> None:
        print(f"Fahrrad lenkt um {winkel}°")
 
 
def slalom(obj: Lenkbar):
    for w in (15, -20, 25):
        obj.lenke(w)
 
 
 
print("Slalom Auto:")
slalom(Auto("VW", "Golf"))
 
print("\nSlalom Fahrrad:")
slalom(Fahrrad())
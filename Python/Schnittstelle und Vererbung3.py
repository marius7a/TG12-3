from abc import ABC, abstractmethod
 
class Fluggeraet(ABC):
 
    @abstractmethod
    def abheben(self) -> None: ...
 
    @abstractmethod
    def landen(self) -> None: ...
 
 
class Drohne(Fluggeraet):
    def abheben(self):
        print("Drohne steigt vertikal auf.")
    def landen(self):
        print("Drohne landet präzise.")
 
 
class Flugzeug(Fluggeraet):
    def abheben(self):
        print("Flugzeug beschleunigt auf der Startbahn.")
    def landen(self):
        print("Flugzeug rollt nach der Landung aus.")
 
 
print("\nDrohne")
d = Drohne()
d.abheben()
d.landen()
 
print("\nFlugzeug")
f = Flugzeug
f.abheben()
f.landen()
 
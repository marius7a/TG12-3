class Akku:
    def __init__(self, kapazitaet_kwh: float):
        self.kapazitaet_kwh = kapazitaet_kwh
        self.stand_prozent = 100.0
 
    def lade_auf(self, kwh: float):
        prozent = (kwh / self.kapazitaet_kwh) * 100
        self.stand_prozent = min(100.0, max(0.0, self.stand_prozent + prozent))
        print(f"Akkustand: {self.stand_prozent:.1f}%")
 
class ElektroAuto:
    def __init__(self, marke: str, modell: str, akku: Akku):
        self.marke = marke
        self.modell = modell
        self.akku = akku
        self.motor_an = False
        self.geschwindigkeit = 0
 
    def starte_motor(self):
        self.motor_an = True
        print(f"{self.marke} {self.modell}: EV-System aktiv.")
 
    def stoppe_motor(self):
        self.motor_an = False
        self.geschwindigkeit = 0
        print(f"{self.marke} {self.modell}: EV-System aus.")
 
    def beschleunige(self, delta: int):
        if not self.motor_an:
            print("System ist aus. Starte das Auto zuerst.")
            return
        self.geschwindigkeit += delta
        print(f"{self.marke} {self.modell}: {self.geschwindigkeit} km/h")
        self.akku.lade_auf(-0.1 * delta)
 
akku = Akku(60)
ev = ElektroAuto("Tesla", "Model 3", akku)
ev.starte_motor()
ev.beschleunige(50)
ev.stoppe_motor()
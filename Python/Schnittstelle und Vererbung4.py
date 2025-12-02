class VerbrennerAuto:
    def __init__(self, marke: str, modell: str):
        self.marke = marke
        self.modell = modell
        self.motor_an = False
        self.geschwindigkeit = 0
 
    def starte_motor(self):
        self.motor_an = True
        print(f"{self.marke} {self.modell}: Motor gestartet.")
 
    def stoppe_motor(self):
        self.motor_an = False
        self.geschwindigkeit = 0
        print(f"{self.marke} {self.modell}: Motor gestoppt.")
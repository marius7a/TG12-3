# client.py
import requests
from model2 import Spieler
from pydantic import ValidationError

SERVER_URL = 'http://localhost:12345/spieler'

def spieler_eingeben_und_senden():
    daten = {
        "name": input("Name: "),
        "alter": input("Alter: "),
        "position": input("Position: "),
        "tore": input("Tore: ")
    }

    try:
        spieler = Spieler(
            name=daten["name"],
            alter=int(daten["alter"]),
            position=daten["position"],
            tore=int(daten["tore"])
        )
    except ValidationError as e:
        print("Fehler bei der Eingabe:", e)
        return
    except ValueError:
        print("Alter und Tore müssen Zahlen sein.")
        return

    res = requests.post(SERVER_URL, json=spieler.model_dump())

    print(res.json())

if __name__ == '__main__':
    spieler_eingeben_und_senden()

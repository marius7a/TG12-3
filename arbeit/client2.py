import requests
from model import Spieler
from pydantic import ValidationError

SERVER_URL = 'http://localhost:12345/spieler'

def spieler_eingeben_und_senden():
    name = input("Name: ")
    alter = input("Alter: ")
    position = input("Position (Torwart, Innenverteidiger, Außenverteidiger, Zentrales Mittelfeld, Flügelspieler, Stürmer): ")
    tore = input("Tore: ")

    try:
        spieler =Spieler(
            name=name,
            alter=int(alter),
            position=position,
            tore=int(tore)
        )
    except ValidationError as e:
        print("Fehler bei der Eingabe:", e)
        return

    response = requests.post(SERVER_URL, json=spieler.dict())
    
    if response.status_code == 201:
        print("Spieler erfolgreich an den Server gesendet:")
        print(response.json())
    else:
        print("Fehler bei der Serverantwort:")
        print(response.json())

if __name__ == '__main__':
    spieler_eingeben_und_senden()

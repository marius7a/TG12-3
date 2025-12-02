from flask import Flask, request, jsonify
from pydantic import ValidationError
from model2 import Spieler

app = Flask(__name__)

@app.route('/spieler', methods=['POST'])
def add_spieler():
    json_data = request.json
    try:
        spieler = Spieler.parse_obj(json_data)
        print(f"Neuer Spieler: {spieler}")
        return jsonify({"message": "Spieler erfolgreich angelegt", "spieler": spieler.dict()}), 201
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)




from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def serve_index():
    return send_from_directory("web", "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory("web", path)

@app.route("/spieler", methods=["POST"])
def spieler_empfangen():
    data = request.get_json()
    name = data.get("name")
    jahrgang = data.get("jahrgang")
    staerke = data.get("staerke")
    torschuss = data.get("torschuss")
    motivation = data.get("motivation")
    position = data.get("position")

    antwort = {
        "status": "ok",
        "message": f"Spieler '{name}' ({jahrgang}) mit Stärke {staerke}, Torschuss {torschuss}, Motivation {motivation} und Position '{position}' wurde erfasst."
    }
    return jsonify(antwort)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

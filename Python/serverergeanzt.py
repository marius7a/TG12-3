from flask import Flask, request, jsonify

app = Flask(__name__)

# Route für die Hauptseite
@app.route('/')
def home():
    return "Server ist bereit und wartet auf Anfragen."

# Route für mein Profil
@app.route('/profil')
def profil():
    return "Marius wildenhof\nHauptstr. 18\n78706 Berlin"

@app.route('/impressum')
def impressum():
    return """
<html>
<head>
<titel>Impressum</titel>
</head>
<body>
<h3>Impressum</h3>
</body>
</html>


"""

# Route zum Empfangen von Nachrichten
@app.route('/message', methods=['POST'])
def handle_message():
    data = request.json
    message = data.get('message', '')
    print(f"Empfangen: {message}")

    # Ausgabe aller wichtigen Request-Attribute
    print("=== Request-Informationen ===")
    print("request.method:", request.method)
    print("request.args:", request.args)  # Query-Parameter
    print("request.form:", request.form)  # Formulardaten (z.B. bei POST-Formularen)
    print("request.json:", request.json)  # JSON-Daten im Body
    print("request.data:", request.data)  # Rohdaten im Body
    print("request.headers:", dict(request.headers))  # Header als Dictionary
    print("request.cookies:", request.cookies)  # Cookies
    print("request.path:", request.path)  # Pfad der URL
    print("request.url:", request.url)  # Volle URL
    print("request.remote_addr:", request.remote_addr)  # IP-Adresse des Clients
    print("=============================")

    response_message = f"Echo: {message}"
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)

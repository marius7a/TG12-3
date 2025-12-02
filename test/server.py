from flask import Flask, request, jsonify
from pydantic import ValidationError
from model import iPad

app = Flask(__name__)

@app.route('Pfad', methods=['POST'])

def add_iPad():
    json_data = request.json






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)

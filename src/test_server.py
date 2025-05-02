"""
Servidor de prueba para manejar solicitudes de API durante las pruebas.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/api/config', methods=['GET'])
def config():
    return jsonify({"debug": True, "log_level": "DEBUG", "api_key": "test_key_123"}), 200

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get("api_key") == "test_key_123":
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid API key"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

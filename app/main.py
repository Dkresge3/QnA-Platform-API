from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the QnA Platform API!"}), 200

@app.route('/api/v1/auth')
def auth_stub():
    return jsonify({"message": "Authentication endpoint stub"}), 200

@app.route('/api/v1/users')
def users_stub():
    return jsonify({"message": "Users endpoint stub"}), 200

@app.route('/api/v1/questions')
def questions_stub():
    return jsonify({"message": "Questions endpoint stub"}), 200

@app.route('/api/v1/answers')
def answers_stub():
    return jsonify({"message": "Answers endpoint stub"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify
from flask_cors import CORS
from app.config import Config
from app.models import db
from app.api import auth_bp, users_bp, questions_bp, answers_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize CORS
    CORS(app)

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(users_bp, url_prefix='/api/v1/users')
    app.register_blueprint(questions_bp, url_prefix='/api/v1/questions')
    app.register_blueprint(answers_bp, url_prefix='/api/v1/answers')

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the QnA Platform API!"}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)


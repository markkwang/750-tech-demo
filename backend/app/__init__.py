from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS

def create_app():
    load_dotenv()

    app = Flask(__name__)
    CORS(app)
    app.config['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app

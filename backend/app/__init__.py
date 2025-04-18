from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app

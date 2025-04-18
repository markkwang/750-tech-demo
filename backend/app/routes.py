from flask import Blueprint, request, jsonify, current_app
from .crawler import extract_text_from_url
from .summariser import ai_summarise_text, test_openai

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the summariser API!"})

@bp.route("/test_crawler", methods=["GET"])
def crawler():
    url = "https://www.bbc.com/"
    page_text = extract_text_from_url(url)
    return jsonify({"text": page_text})

@bp.route("/test_openai_x", methods=["GET"])
def openai_x():
    prompt = "Expand the following text: 'The quick brown fox jumps over the lazy dog.'"
    summary = test_openai(prompt)
    return jsonify({"summary": summary})

@bp.route("/test_openai_y", methods=["GET"])
def openai_y():
    prompt = "Now, repeat the prevous answer. Then, expand it more."
    summary = test_openai(prompt)
    return jsonify({"summary": summary})

@bp.route("/summarise", methods=["POST"])
def summarise():
    pass
    # data = request.get_json()
    # url = data.get("url")

    # if not url:
    #     return jsonify({"error": "Missing URL"}), 400

    # try:
    #     page_text = extract_text_from_url(url)
    #     summary = summarise_text(page_text, current_app.config["OPENAI_API_KEY"])
    #     return jsonify({"summary": summary})
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500

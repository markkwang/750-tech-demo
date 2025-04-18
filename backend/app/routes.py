from flask import Blueprint, request, jsonify, current_app
from .crawler import extract_text_from_url
from .summariser import ai_analyse_text, test_openai

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
    data = request.get_json()
    print(data)
    prompt = "Expand the following text: 'The quick brown fox jumps over the lazy dog.'"
    response = test_openai(prompt)
    return jsonify({"response": response})

@bp.route("/test_openai_y", methods=["GET"])
def openai_y():
    prompt = "Now, repeat the prevous answer. Then, expand it more."
    response = test_openai(prompt)
    return jsonify({"response": response})

@bp.route("/summarise_web", methods=["POST"])
def summarise():

    data = request.get_json()
    url = data.get("message")

    if not url:
        return jsonify({"response": "Missing message"}), 400
    
    try:
        page_text = extract_text_from_url(url)
        response = ai_analyse_text(page_text)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": str(e)}), 500
    
@bp.route("/messages_to_gpt", methods=["POST"])
def messages_to_gpt():
    data = request.get_json()
    messages = data.get("message")

    if not messages:
        return jsonify({"response": "Missing messages"}), 400

    try:
        response = ai_analyse_text(messages)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": str(e)}), 500

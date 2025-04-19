from flask import Blueprint, request, jsonify, Response
from .crawler import extract_text_from_url_all, extract_text_from_url_customised, extract_text_from_url_login, extract_text_from_url_session
from .summariser import ai_analyse_text, test_openai
from markupsafe import escape

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the summariser API!"})

@bp.route("/test_crawler_bbc", methods=["GET"])
def crawler_bbc():
    url = "https://www.bbc.com/"
    page_text = extract_text_from_url_all(url)
    return jsonify({"text": page_text})

@bp.route("/test_crawler_filtered", methods=["GET"])
def crawler_1():
    url = "https://quotes.toscrape.com/"
    list = extract_text_from_url_customised(url)
    return jsonify({"quotes": list})

@bp.route("/test_crawler_login", methods=["GET"])
def crawler_login():
    url = "https://the-internet.herokuapp.com/authenticate"
    secure_url = "https://the-internet.herokuapp.com/secure"
    page_text = extract_text_from_url_login(url, secure_url)
    
    pretty = f"""
    <h2>Request 1:</h2>
    <pre>{escape(page_text["request1"])}</pre>
    <h2>Request 2:</h2>
    <pre>{escape(page_text["request2"])}</pre>
    """
    return Response(pretty, content_type="text/html")


@bp.route("/test_crawler_session", methods=["GET"])
def crawler_session():
    url = "https://the-internet.herokuapp.com/authenticate"
    secure_url = "https://the-internet.herokuapp.com/secure"
    page_text = extract_text_from_url_session(url, secure_url)
    
    pretty = f"""
    <h2>Request 1:</h2>
    <pre>{escape(page_text["request1"])}</pre>
    <h2>Request 2:</h2>
    <pre>{escape(page_text["request2"])}</pre>
    """
    return Response(pretty, content_type="text/html")

@bp.route("/test_openai", methods=["GET"])
def openai_x():
    prompt = "Expand the following text: 'The quick brown fox jumps over the lazy dog.'"
    response = test_openai(prompt)
    return jsonify({"response": response})

@bp.route("/summarise_web", methods=["POST"])
def summarise():

    data = request.get_json()
    url = data.get("message")

    if not url:
        return jsonify({"response": "Missing message"}), 400
    
    try:
        page_text = extract_text_from_url_all(url)
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

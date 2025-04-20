from flask import Blueprint, request, jsonify, Response
from .crawler import extract_text_from_url_all, extract_text_from_url_customised, extract_text_from_url_login, extract_text_from_url_session, extract_text_from_url_raw
from .summariser import ai_analyse_text, test_openai
from markupsafe import escape
import json

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the summariser API!"})

@bp.route("/test_crawler_bbc_1", methods=["GET"])
def crawler_bbc_1():
    url = "https://www.bbc.com/"
    page_text = extract_text_from_url_raw(url)
    pretty = f"""
    <h2>Request to bbc</h2>
    <pre>{escape(page_text["url"])}</pre>
    <h2>Content</h2>
    <pre>{escape(page_text["html"])}</pre>
    """
    return Response(pretty, content_type="text/html")

@bp.route("/test_crawler_bbc_2", methods=["GET"])
def crawler_bbc_2():
    url = "https://www.bbc.com/"
    page_text = extract_text_from_url_all(url)
    pretty = f"""
    <h2>Request to bbc</h2>
    <pre>{escape(page_text["url"])}</pre>
    <h2>Content</h2>
    <pre>{escape(page_text["html"])}</pre>
    """
    return Response(pretty, content_type="text/html")

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
    prompt = "'The quick and nimble brown fox, full of energy and curiosity, gracefully leaps over the sleepy, sluggish dog who lies basking in the warm afternoon sun without a care in the world.'"
    response = test_openai(prompt)
    return jsonify({"response": response})
    
@bp.route("/messages_to_gpt", methods=["POST"])
def messages_to_gpt():
    data = request.get_json()
    messages = data.get("message")

    if not messages:
        return jsonify({"response": "Missing messages"}), 400

    try:
        if messages.startswith("https"):
            page_text = extract_text_from_url_all(messages)
            response = ai_analyse_text(json.dumps(page_text)) 
        else:
            response = ai_analyse_text(messages)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": str(e)}), 500

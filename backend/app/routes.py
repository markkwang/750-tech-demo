from flask import Blueprint, request, jsonify, current_app
# from .crawler import extract_text_from_url
# from .summariser import summarise_text

bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the summariser API!"})

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

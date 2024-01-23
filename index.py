from flask import Flask, request, jsonify

from html_utils import strip_tags
from language_detector import getLangData
from api_service import fetchAPI

app = Flask(__name__)

@app.route("/lang-detect", methods=["POST"])
def handle_post():
    # get work item id
    data = request.get_json()
    workId = data["resource"]["id"]

    # get work item description
    fetchedWork = fetchAPI("GET", workId, "&$expand=all")
    print("🚀 ~ fetchedWork:", fetchedWork)
    text = strip_tags(fetchedWork["fields"]["System.Description"])

    # detect language
    lang_data = getLangData(text)

    # if language is not english
    if lang_data["confidence"] > 0.7 and not lang_data["isEnglish"]:
        # add tag
        fetchAPI("PATCH", workId, "", [{"op": "add", "path": "/fields/System.Tags", "value": "Lang"}])

    return jsonify(lang_data), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)

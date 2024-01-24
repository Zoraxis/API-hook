from flask import Flask, request, jsonify

from html_utils import strip_tags
from language_detector import isLanguageFalse
from api_service import fetchAPI

app = Flask(__name__)

@app.route("/lang-detect", methods=["POST"])
def handle_create():
    # get work item id
    data = request.get_json()
    workId = data["resource"]["id"]
    print("🚀 ~ handle_create ~ workId", workId)

    # get work item description
    fetchedWork = fetchAPI("GET", workId, "&$expand=all")
    print("🚀 ~ handle_create ~ fetchedWork", fetchedWork)
    text = strip_tags(fetchedWork["fields"]["System.Description"])

    print("🚀 ~ handle_create ~ text", text)
    # if language is not acceptable
    if isLanguageFalse(text):
        # add tag
        fetchAPI("PATCH", workId, "", [{"op": "add", "path": "/fields/System.Tags", "value": "Lang"}])

    return text, 200

@app.route("/lang-detect/update", methods=["POST"])
def handle_update():
    data = request.get_json()
    print("🚀 ~ handle_update")
    return 'handle_update', 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)

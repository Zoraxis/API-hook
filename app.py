from flask import Flask, request

from services.routing_service import handle_work_create

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "ok", 200

@app.route("/lang-detect", methods=["GET"])
def create_index():
    return "wrong method", 200

@app.route("/lang-detect", methods=["POST"])
def handle_create():
    data = request.get_json()
    response = handle_work_create(data)
    return response, 200

@app.route("/lang-detect/update", methods=["POST"])
def handle_update():
    data = request.get_json()
    response = handle_work_create(data)
    return response, 200

if __name__ == "__main__":
    app.run()

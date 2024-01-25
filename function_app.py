import azure.functions as func
from flask import Flask, request

from services.routing_service import handle_work_create

app = Flask(__name__)

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

app = func.WsgiFunctionApp(app=app.wsgi_app, 
                           http_auth_level=func.AuthLevel.ANONYMOUS)
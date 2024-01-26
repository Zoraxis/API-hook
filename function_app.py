import azure.functions as func
import logging
from flask import Flask, request
from ..FlaskApp.wsgi import application

from services.routing_service import handle_work_create

app = func.FunctionApp()

@app.route(route="http_trigger", auth_level=func.AuthLevel.undefined)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
# app = Flask(__name__)

# @app.route("/lang-detect", methods=["POST"])
# def handle_create():
#     data = request.get_json()
#     response = handle_work_create(data)
#     return response, 200

# @app.route("/lang-detect/update", methods=["POST"])
# def handle_update():
#     data = request.get_json()
#     response = handle_work_create(data)
#     return response, 200

# app = func.WsgiFunctionApp(app=app.wsgi_app, 
                        #    http_auth_level=func.AuthLevel.ANONYMOUS)
# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')
#     uri=req.params['uri']
#     with app.test_client() as c:
#         doAction = {
#             "GET": c.get(uri).data,
#             "POST": c.post(uri).data
#         }
#         resp = doAction.get(req.method).decode()
#         return func.HttpResponse(resp, mimetype='text/html')

# main = func.WsgiMiddleware(application).main
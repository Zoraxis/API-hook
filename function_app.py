# import azure.functions as func
# import logging
import sys
from sys import path
import os
import logging

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)

# app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# @app.route(route="http_trigger")
# def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')
#     req_body = req.get_json()
#     response = handle_work_create(req_body)

#     return func.HttpResponse(
#              response,
#              status_code=200
#         )

import azure.functions as func
from customServices.routing_service import handle_work_create

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="work_trigget")
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
import azure.functions as func
import logging

from services.routing_service import handle_work_create

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    response = handle_work_create(req_body)

    return func.HttpResponse(
             response,
             status_code=200
        )
import logging
import azure.functions as func

from services import routing_service

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="work_trigget")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    response = routing_service.handle_work_create(req_body)

    return func.HttpResponse(
             response,
             status_code=200
        )
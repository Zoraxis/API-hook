import logging
import azure.functions as func

import settings

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="work_trigget")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()

    return func.HttpResponse(
             "dwd",
             status_code=200
        )
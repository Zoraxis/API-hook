from azure.functions import func

from services.routing_service import handle_work_create

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="lang-detect")
def handle_create(req: func.HttpRequest):
    data = req.params.get('body')
    # response = handle_work_create(data)
    return data, 200

# @app.route("/lang-detect/update", methods=["POST"])
# def handle_update():
#     data = request.get_json()
#     response = handle_work_create(data)
#     return response, 200

from services.html_service import strip_tags
from services.language_service import isLanguageFalse
from services.api_service import fetchAPI
from settings import getEnv

field = getEnv("PATCH_FIELD")
value = getEnv("PATCH_VALUE")

def handle_work_create(data):
    # get work item id
    workId = data["resource"]["id"]

    # get work item description
    fetchedWork = fetchAPI("GET", workId, "&$expand=all")
    text = strip_tags(fetchedWork["fields"]["System.Description"])

    # if language is not acceptable
    if isLanguageFalse(text):
        # add tag
        fetchAPI("PATCH", workId, "", [
            {
                "op": "add", 
                "path": f"/fields/{field}", 
                "value": value
            }
        ])

    return text

def handle_work_update(data):
    print("🚀 ~ handle_update")

    return "handle_work_update"
import html_service
import language_service
import api_service
import settings

field = settings.getEnv("PATCH_FIELD")
value = settings.getEnv("PATCH_VALUE")

def handle_work_create(data):
    # get work item id
    workId = data["resource"]["id"]

    # get work item description
    fetchedWork = api_service.fetchAPI("GET", workId, "&$expand=all")
    text = html_service.strip_tags(fetchedWork["fields"]["System.Description"])

    # if language is not acceptable
    if language_service.isLanguageFalse(text):
        # add tag
        api_service.fetchAPI("PATCH", workId, "", [
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
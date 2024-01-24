import requests
import base64

devopsURL = "https://dev.azure.com/ZorkTest/TEST/_apis/wit/workitems/"
apiURL = "?api-version=7.1-preview.3"
PAT = "tjn4acl5h42muqr472jqjsr5mkbmndr5ambhjdafuatoqseixo3a"
PAT_encoded = base64.b64encode((":" + PAT).encode()).decode()

def fetchAPI(method, workId = 10, extra = "", body = {}):
    patchURL = devopsURL + str(workId) + apiURL + extra
    req = requests.request(
        method,
        patchURL,
        json=body,
        headers={
            "Authorization": "Basic " + PAT_encoded,
            "Content-Type": "application/json-patch+json",
        },
    )

    try:
        return req.json()
    except requests.exceptions.JSONDecodeError:
        print("Received an empty response")
        return None
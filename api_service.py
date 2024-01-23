import requests
import base64

devopsURL = "https://dev.azure.com/ZorkTest/TEST/_apis/wit/workitems/"
apiURL = "?api-version=7.1-preview.3"
PAT = "oufhhic3by73oh5fqqpjgeorgcj2co6p4pv4dopmo75kuxxvlwra"
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
    return req.json()
import requests
import base64
from settings import getEnv

devopsURL = getEnv("DEVOPS_URL")
apiURL = getEnv("DEVOPS_VERSION")
PAT = getEnv("DEVOPS_PAT")

PAT_encoded = base64.b64encode((":" + PAT).encode()).decode()

def fetchAPI(method, workId = 10, extra = "", body = {}):
    patchURL = f"{devopsURL}{str(workId)}{apiURL}{extra}"
    req = requests.request(
        method,
        patchURL,
        json=body,
        headers={
            "Authorization": f"Basic {PAT_encoded}",
            "Content-Type": "application/json-patch+json",
        },
    )

    try:
        return req.json()
    except requests.exceptions.JSONDecodeError:
        print("Received an empty response")
        return None
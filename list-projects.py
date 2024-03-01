import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://rachanaav01.atlassian.net/rest/api/3/project"

API_TOKEN = ""

auth = HTTPBasicAuth("", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
for obj in output:
    print(obj["name"])
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
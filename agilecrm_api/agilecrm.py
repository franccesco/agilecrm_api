import json
import requests
from os import getenv
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

# Loading environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY = getenv('API_KEY')
EMAIL = getenv('EMAIL')
DOMAIN = getenv('DOMAIN')
API_URL = f'https://" + {DOMAIN} + ".agilecrm.com/dev/api/'


def agileCRM(path, http_method, data, content_type):

    url = API_URL + path
    headers = {'Accept': 'application/json', 'content-type': content_type}
    creds = EMAIL, API_KEY

    if http_method == "GET":
        response = requests.get(url, headers=headers, auth=creds)
        return response.text

    if http_method == "POST":
        response = requests.post(url, data=json.dumps(data), headers=headers, auth=creds)
        return response.text

    if http_method == "PUT":
        response = requests.put(url, data=json.dumps(data), headers=headers, auth=creds)
        return response.text

    if http_method == "DELETE":
        response = requests.delete(url, headers=headers, auth=creds)
        return response

    if http_method == "POSTFORM":
        response = requests.post(url, data=data, headers=headers, auth=creds)
        return response.text

    raise ValueError(f'Wrong HTTP Method: {http_method}')

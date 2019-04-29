import requests
import json

APIKEY = "***********"   # Your API KEY
EMAIL = "sample@agilecrm.com"  # Your API EMAIL
DOMAIN = "sample"  # Your DOMAIN
API_URL = f'https://" + {DOMAIN} + ".agilecrm.com/dev/api/'


def agileCRM(path, http_method, data, content_type):

    url = API_URL + path
    headers = {'Accept': 'application/json', 'content-type': content_type}

    if http_method == "GET":
        response = requests.get(url, headers=headers, auth=(EMAIL, APIKEY))
        return response.text

    if http_method == "POST":
        response = requests.post(url, data=json.dumps(data), headers=headers, auth=(EMAIL, APIKEY))
        return response.text

    if http_method == "PUT":
        response = requests.put(url, data=json.dumps(data), headers=headers, auth=(EMAIL, APIKEY))
        return response.text

    if http_method == "DELETE":
        response = requests.delete(url, headers=headers, auth=(EMAIL, APIKEY))
        return response

    if http_method == "POSTFORM":
        response = requests.post(url, data=data, headers=headers, auth=(EMAIL, APIKEY))
        return response.text

    raise ValueError(f'Wrong HTTP Method: {http_method}')

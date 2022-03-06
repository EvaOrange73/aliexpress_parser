import json
import pprint

import requests


def send_request(body):
    answer = requests.post('http://localhost:8000/', data=body)
    answer = json.loads(answer.text)
    pprint.pprint(answer, indent=4, sort_dicts=False)


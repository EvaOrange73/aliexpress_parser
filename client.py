import pprint
import sys
import json

import requests


def client():
    print("Hello!\n"
          "I will return the first 10 search results on aliexpress.com\n"
          "I can process requests in json format, for example:\n"
          "{\"searchWord\": \"iphone\"}")

    request = ""
    waiting_for_the_next_line = False

    for line in sys.stdin:
        if line.startswith("{"):
            waiting_for_the_next_line = True

        if waiting_for_the_next_line:
            request += line
        else:
            print("maybe you forgot \"{\"")

        if line.endswith("}\n"):
            waiting_for_the_next_line = False
            try:
                request = json.loads(request)
            except ValueError as e:
                print("I need json format")
                request = ""
                continue

            if request.get("searchWord") is None:
                print("i need searchWord")
                request = ""
                continue

            answer = requests.post('http://localhost:8000/', data=json.dumps(request))
            answer = json.loads(answer.text)
            pprint.pprint(answer, indent=4, sort_dicts=False)

            request = ""


client()

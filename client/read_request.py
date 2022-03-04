import sys
import json

from client.send_request import send_request


def read_request():
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

            send_request(json.dumps(request))

            request = ""


read_request()

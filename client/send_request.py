import requests


def send_request(body):
    answer = requests.post('http://localhost:8000/', data=body)
    print(answer.text)

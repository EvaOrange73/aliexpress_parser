import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

import simplejson


class HttpHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body.decode('utf8'))
        answer = str(json.loads(post_body.decode('utf8')).get("searchWord"))
        self.wfile.write(answer.encode(encoding='utf_8'))


def run_server(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run_server()

#!/usr/bin/python3
import os

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

hostName = "0.0.0.0"
serverPort = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.protocol_version = 'HTTP/1.0'
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("/root/myapp/files/index.html", "rb") as fh:
                content = fh.read()
            self.wfile.write(content)
        else:
            self.send_response(404)
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread"""

if __name__== "__main__":
    werbserver = ThreadedHTTPServer((hostName, serverPort), Handler)
    print ("Server started http://{}:{}".format(hostName, serverPort))

    try:
        werbserver.serve_forever()
    except KeyboardInterrupt:
        pass

    werbserver.server_close()
    print("Server stopped!!!")

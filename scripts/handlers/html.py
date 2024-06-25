import http.server
from io import BufferedReader
import os


def html(handlerClass: http.server.BaseHTTPRequestHandler):
    file: BufferedReader
    handlerClass.send_response(200)
    handlerClass.send_header("Content-Type", "text/html")
    handlerClass.end_headers()

    if handlerClass.path == "/":
        file = open(os.path.join("web", "index.html"), "rb")
    else:
        file = open(os.path.join("web", handlerClass.path), "rb")

    handlerClass.wfile.write(file.read())

    file.close()

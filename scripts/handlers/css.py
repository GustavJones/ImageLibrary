import http.server
import os


def css(handlerClass: http.server.BaseHTTPRequestHandler):
    handlerClass.send_response(200)
    handlerClass.send_header("Content-Type", "text/css")
    handlerClass.end_headers()

    cssFile = open(os.path.join("web", "style.css"), "rb")

    handlerClass.wfile.write(cssFile.read())

    cssFile.close()

import http.server


def jpg(handlerClass: http.server.BaseHTTPRequestHandler):
    fileName: str

    handlerClass.send_response(200)
    handlerClass.send_header("Content-Type", "image/jpg")
    handlerClass.end_headers()

    if handlerClass.path.find("/asset/") != -1:
        fileName = handlerClass.path.replace("/asset", "")

        file = open("library" + fileName, "rb")
        handlerClass.wfile.write(file.read())

        file.close()
    elif handlerClass.path.find("/images/") != -1:
        fileName = handlerClass.path

        file = open("web" + fileName, "rb")
        handlerClass.wfile.write(file.read())

        file.close()

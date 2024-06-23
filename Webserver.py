import http.server
import Types

PORT = 8080


class WebserverRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        sentResponse: bool = False

        for handler in Types.types():
            handlerStr = str(handler).split()[1]
            if self.path.find("." + handlerStr) != -1:
                handler(self)
                sentResponse = True

            elif self.path.find("." + handlerStr.upper()) != -1:
                handler(self)
                sentResponse = True
            elif self.path == "/" and handlerStr == "html":
                handler(self)
                sentResponse = True

        if not sentResponse:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()


class Webserver(object):
    def __init__(self):
        self.webserver = http.server.HTTPServer(
            ("0.0.0.0", PORT), WebserverRequestHandler
        )

    def Close(self):
        self.webserver.shutdown()

    def Run(self):
        try:
            print("Running server on 0.0.0.0:", PORT)
            self.webserver.serve_forever()
        except KeyboardInterrupt:
            self.Close()
            print("\nClosed server")

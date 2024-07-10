import http.server
from io import BytesIO
import PIL.Image
import PIL.ExifTags
import os

COMPRESSED_SCALE = 0.1


def jpg(handlerClass: http.server.BaseHTTPRequestHandler):
    fileName: str

    handlerClass.send_response(200)
    handlerClass.send_header("Content-Type", "image/jpg")
    handlerClass.end_headers()

    if handlerClass.path.find("/asset/") != -1:
        if handlerClass.path.find("[compress]") != -1:
            fileName: str
            fileSize: tuple
            resizedFile: PIL.Image.Image
            resizeSize: tuple[int, int]
            fileExif: PIL.Image.Exif
            output: BytesIO

            output = BytesIO()

            fileName = handlerClass.path.replace("[compress]", "")
            fileName = fileName.replace("/asset/", "")

            file = PIL.Image.open(os.path.join("library", fileName))
            fileSize = file.size

            fileExif = file.getexif()

            resizeSize = (
                int(fileSize[0] * COMPRESSED_SCALE),
                int(fileSize[1] * COMPRESSED_SCALE),
            )

            resizedFile = file.resize(resizeSize)
            resizedFile.save(output, "JPEG", exif=fileExif)

            handlerClass.wfile.write(output.getvalue())

            file.close()
            resizedFile.close()
            output.close()
        else:
            fileName = handlerClass.path.replace("/asset/", "")

            file = open(os.path.join("library", fileName), "rb")
            handlerClass.wfile.write(file.read())

            file.close()

    elif handlerClass.path.find("/images/") != -1:
        if handlerClass.path.find("[compress]") != -1:
            fileName: str
            fileSize: tuple
            resizedFile: PIL.Image.Image
            resizeSize: tuple[int, int]
            fileExif: PIL.Image.Exif
            output: BytesIO

            output = BytesIO()

            fileName = handlerClass.path.replace("[compress]", "")

            file = PIL.Image.open("web" + fileName)
            fileSize = file.size

            fileExif = file.getexif()

            resizeSize = (
                int(fileSize[0] * COMPRESSED_SCALE),
                int(fileSize[1] * COMPRESSED_SCALE),
            )

            resizedFile = file.resize(resizeSize)
            resizedFile.save(output, "JPEG", exif=fileExif)

            handlerClass.wfile.write(output.getvalue())

            file.close()
            resizedFile.close()
            output.close()
        else:
            fileName = handlerClass.path
            file = open(os.path.join("web" + fileName), "rb")
            handlerClass.wfile.write(file.read())

            file.close()

import os
import PIL.Image
from PIL.ExifTags import TAGS


class Image(object):
    def __init__(self) -> None:
        self.name = ""
        self.path = ""
        self.date = ""

        self.image = None

        self.metadata = {}
        self.exifdata = None

    def LoadMetaData(self, path: str):
        self.path = os.path.abspath(path)

        if os.path.exists(self.path) and os.path.isfile(self.path):
            self.name = os.path.basename(self.path)
            try:
                self.image = PIL.Image.open(self.path)
                self.exifdata = self.image.getexif()

                for tagid in self.exifdata:
                    self.metadata[TAGS.get(tagid, tagid)] = self.exifdata.get(tagid)

                self.image.close()

                self.date = self.metadata["DateTime"].split(" ")[0]
            except Exception as e:
                print(e.args)

import os
import scripts.Image as Image


class Library(object):
    def __init__(self, libraryPath: str = "") -> None:
        self.images: list[Image.Image] = []
        self.currentImageIndex = 0

        self.libraryPath = os.path.abspath(libraryPath)
        if not os.path.exists(self.libraryPath):
            os.mkdir(self.libraryPath)

    def SetLibraryPath(self, path: str) -> None:
        self.libraryPath = os.path.abspath(path)
        if not os.path.exists(self.libraryPath):
            os.mkdir(self.libraryPath)

    def GetLibraryPath(self) -> str:
        return self.libraryPath

    def CreateFolder(self) -> None:
        if not os.path.exists(
            os.path.join(self.libraryPath, self.images[self.currentImageIndex].date)
        ):
            os.mkdir(
                os.path.join(self.libraryPath, self.images[self.currentImageIndex].date)
            )

    def CopyToFolder(self) -> bool:
        if not os.path.exists(
            os.path.join(
                self.libraryPath,
                self.images[self.currentImageIndex].date,
                self.images[self.currentImageIndex].name,
            )
        ):
            file = open(self.images[self.currentImageIndex].path, "rb")
            fileCopy = open(
                os.path.join(
                    self.libraryPath,
                    self.images[self.currentImageIndex].date,
                    self.images[self.currentImageIndex].name,
                ),
                "xb",
            )

            fileCopy.write(file.read())

            file.close()
            fileCopy.close()

            return True

        else:
            return False

    def AddImage(self, path: str) -> bool:
        image: Image.Image

        image = Image.Image()
        image.LoadMetaData(path)

        # If no metadata exit
        if image.metadata == {}:
            return False

        self.images.append(image)
        self.currentImageIndex = len(self.images) - 1

        self.CreateFolder()
        self.CopyToFolder()

        return True

    def AddDirectory(self, path: str) -> None:
        directoryPath: str
        directoryItems: list[str]

        directoryPath = os.path.abspath(path)
        directoryItems = os.listdir(directoryPath)

        for i in directoryItems:
            if (
                os.path.isfile(os.path.join(directoryPath, i))
                and (
                    os.path.join(directoryPath, i).find(".JPG") != -1
                    or os.path.join(directoryPath, i).find(".jpg") != -1
                )
                and (
                    os.path.join(directoryPath, i)[-1] == "g"
                    or os.path.join(directoryPath, i)[-1] == "G"
                )
            ):
                if not self.AddImage(os.path.join(directoryPath, i)):
                    # For all other files
                    pass
            elif os.path.isdir(os.path.join(directoryPath, i)):
                self.AddDirectory(os.path.join(directoryPath, i))

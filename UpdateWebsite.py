from io import TextIOWrapper
import os


def UpdateWebsite() -> None:
    dateFile: TextIOWrapper
    libraryFile: TextIOWrapper
    imagesOut: str = ""
    dateOut: str = ""
    folderOut: str = ""
    libraryOut: str = ""

    datesList: list[str]
    imagesList: list[str]

    datesList = os.listdir(os.path.join("library"))
    datesList.sort()

    for date in datesList:
        imagesOut = ""
        dateOut = ""

        imagesList = os.listdir(os.path.join("library", date))
        imagesList.sort()

        # Get Images for every Date
        for img in imagesList:
            imagesOut += SetImageBuffer("/asset" + "/" + date + "/" + img) + "\n\n"

        dateOut = SetDateBuffer(imagesOut)

        if not os.path.exists(os.path.join("web", "folders", date + ".html")):
            open(os.path.join("web", "folders", date + ".html"), "x").close()

        dateFile = open(os.path.join("web", "folders", date + ".html"), "w")
        dateFile.write(dateOut)
        dateFile.close()

        # TODO
        # Add date .html file to library.html

        folderOut += SetFolderBuffer(date) + "\n\n"

    libraryOut = SetLibraryBuffer(folderOut)
    libraryFile = open(os.path.join("web", "library.html"), "w")
    libraryFile.write(libraryOut)
    libraryFile.close()


def SetImageBuffer(path: str) -> str:
    templateImageFile: TextIOWrapper
    imageBufferList: list[str]
    imageBuffer: str

    templateImageFile = open(os.path.join("web", "templates", "image.html"), "r")
    imageBufferList = templateImageFile.read().split("<!-- $INSERT -->")

    for i in range(len(imageBufferList) - 1):
        if imageBufferList[i].find("<!-- $IMAGE_PATH -->") != -1:
            imageBufferList[i] = path

    imageBuffer = ""
    for substr in imageBufferList:
        imageBuffer += substr

    templateImageFile.close()

    return imageBuffer


def SetDateBuffer(images: str) -> str:
    templateDateFile: TextIOWrapper
    dateBufferList: list[str]
    dateBuffer: str

    templateDateFile = open(os.path.join("web", "templates", "date.html"), "r")

    dateBufferList = templateDateFile.read().split("<!-- $INSERT -->")

    for i in range(len(dateBufferList) - 1):
        if dateBufferList[i].find("<!-- $IMAGE -->") != -1:
            dateBufferList[i] = images

    dateBuffer = ""
    for substr in dateBufferList:
        dateBuffer += substr

    templateDateFile.close()

    return dateBuffer


def SetFolderBuffer(date: str):
    templateFolderFile: TextIOWrapper
    folderBufferList: list[str]
    folderBuffer: str

    templateFolderFile = open(os.path.join("web", "templates", "folder.html"), "r")
    folderBufferList = templateFolderFile.read().split("<!-- $INSERT -->")

    for i in range(len(folderBufferList) - 1):
        if folderBufferList[i].find("<!-- $DATE -->") != -1:
            folderBufferList[i] = date

    folderBuffer = ""
    for substr in folderBufferList:
        folderBuffer += substr

    templateFolderFile.close()

    return folderBuffer


def SetLibraryBuffer(folder: str):
    templateLibraryFile: TextIOWrapper
    libraryBufferList: list[str]
    libraryBuffer: str

    templateLibraryFile = open(os.path.join("web", "templates", "library.html"), "r")

    libraryBufferList = templateLibraryFile.read().split("<!-- $INSERT -->")

    for i in range(len(libraryBufferList) - 1):
        if libraryBufferList[i].find("<!-- $FOLDER -->") != -1:
            libraryBufferList[i] = folder

    libraryBuffer = ""
    for substr in libraryBufferList:
        libraryBuffer += substr

    templateLibraryFile.close()

    return libraryBuffer

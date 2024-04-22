import os
import Library
import Webserver

includedPaths: list[str] = []
includedPathsFile: str = os.path.join("LibraryPaths.txt")

if __name__ == "__main__":
    webserver = Webserver.Webserver()

    library = Library.Library("library/")

    if os.path.exists(includedPathsFile) and os.path.isfile(
        os.path.join(includedPathsFile)
    ):
        file = open(includedPathsFile, "r")

        includedPaths = file.read().split("\n")
    else:
        open(includedPathsFile, "x").close()

    for path in includedPaths:
        if path.find("~") != -1:
            library.AddDirectory(path.replace("~", os.environ["HOME"]))
        else:
            library.AddDirectory(path)

    webserver.Run()

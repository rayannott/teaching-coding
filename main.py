import pathlib

from network import Network
from gui import NetworkApp


SAVES_DIR = pathlib.Path("saves")


if __name__ == "__main__":
    app = NetworkApp()
    app.run()

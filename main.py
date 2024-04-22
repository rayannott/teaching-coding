import pathlib

from network import Network
from gui import NetworkGui


SAVES_DIR = pathlib.Path("saves")


if __name__ == "__main__":
    app = NetworkGui()
    app.run()

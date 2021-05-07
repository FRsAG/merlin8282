import sys
from .constants import Constants


class System(Constants):
    def __init__(self):
        super().__init__()

    def quit(self):
        sys.exit(self.EXIT_CODE)

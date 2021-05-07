from .constants import Constants


class Logger(Constants):
    def __init__(self):
        super().__init__()

    def log(self):
        print(self.MESSAGE)

import sys
from .errors import PythonVersionError
from .constants import Constants


class Checker(Constants):
    def __init__(self):
        super().__init__()
        self.version = sys.version_info

    def check_python_version(self):
        min_version = self.MIN_VERSION
        if self.version < min_version:
            version_string = ".".join(str(_) for _ in min_version)
            raise PythonVersionError(f"Python >= {version_string} required.")

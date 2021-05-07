#!/usr/bin/env python3

import sys


class PythonVersionError(Exception):
    pass


if sys.version_info < (3, 6):
    raise PythonVersionError("Python >= 3.6 required.")

MESSAGE = "AZY TA SOEUR ELLE CROIT QU'UNE ERREUR 808 C'EST 2 ERREURS 404 !"


if __name__ == "__main__":
    print(f"{MESSAGE}")
    sys.exit(42)

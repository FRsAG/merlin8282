class Constants:
    def __init__(self):
        self.MIN_VERSION = (3, 8)
        self._base_errorcode = 404
        self.multiplier = 2
        self.MESSAGE = "AZY TA SOEUR ELLE CROIT QU'UNE ERREUR "
        self.MESSAGE += f"{self._base_errorcode * self.multiplier} "
        self.MESSAGE += f"C'EST {self.multiplier} "
        self.MESSAGE += f"ERREURS {self._base_errorcode} !"
        self.EXIT_CODE = 42

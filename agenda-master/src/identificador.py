from enum import Enum

class Identificador(Enum):
    CELULAR = ("Celular")
    CASA = ("Casa")
    TRABALHO = ("Trabalho")

    def _init_(self, nome:str):
        self.identificador = nome
from enum import Enum

class Genero(Enum):
    MASCULINO = ("M", "Masculino")
    FEMININO = ("F", "Feminino")

    def __init__(self,carac: str,sexualidade: str) -> None:
        self.carc = carac
        self.sexualidade = sexualidade
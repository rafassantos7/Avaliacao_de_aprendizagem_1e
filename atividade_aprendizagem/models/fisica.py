from ..models.endereco import Endereco
from ..models.pessoa import Pessoa
from ..models.enums.sexo import Sexo
from ..models.enums.estado_civil import EstadoCivil
from abc import ABC, abstractmethod

class Fisica(Pessoa,ABC):
    def __init__(self,id: int, nome: str, telefone: str, email: str, endereco: Endereco,sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento

    @abstractmethod
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nSexo: {self.sexo.texto}/{self.sexo.caractere}"
            f"\nEstado Civil: {self.estadoCivil.texto}"
            f"\nData de Nascimento: {self.dataNascimento}"            
            )
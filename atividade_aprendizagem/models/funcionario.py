from abc import ABC, abstractmethod
from models.endereco import Endereco
from models.enums.estado_civil import EstadoCivil
from models.enums.sexo import Sexo
from models.fisica import Fisica
from models.enums.setor import Setor

class Funcionario(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str,cpf: str, rg: str,matricula: str,setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario


    @abstractmethod
    def __str__(self) -> str:
        return (f"Cpf: {self.cpf}"
                f"\nRg: {self.rg}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor.name}"
                f"\nSalario: {self.salario}"
        )

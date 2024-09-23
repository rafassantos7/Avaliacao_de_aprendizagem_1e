from abc import ABC, abstractmethod
from ..models.endereco import Endereco
from ..models.enums.estado_civil import EstadoCivil
from ..models.enums.sexo import Sexo
from ..models.fisica import Fisica
from ..models.enums.setor import Setor

class Funcionario(Fisica):
    def __init__(self,id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str,cpf: str, rg: str,matricula: str,setor: Setor, salario: float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = self._verificar_salario(salario)

    def _verificar_salario(self,salario):
        if not isinstance(salario,float):
            raise TypeError("O salário deve ser em float.")
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        return salario

    @abstractmethod
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCpf: {self.cpf}"
                f"\nRg: {self.rg}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor.nome}"
                f"\nSalario: {self.salario}")
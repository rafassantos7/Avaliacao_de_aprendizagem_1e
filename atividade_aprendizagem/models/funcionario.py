from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self,cpf: str,rg: str, matricula: str, setor: Setor, salario: float) -> None:
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
                f"\nSetor: {self.setor}"
                f"\nSalario: {self.salario}"
        )

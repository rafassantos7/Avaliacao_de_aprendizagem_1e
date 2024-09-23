from models.endereco import Endereco
from models.enums.estado_civil import EstadoCivil
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.funcionario import Funcionario

class Advogado(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, oab: str) -> None:
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.oab = oab

    def __str__(self) -> str:
        return f"{super().__str__()}\nOab: {self.oab}"
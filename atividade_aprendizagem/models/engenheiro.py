from atividade_aprendizagem.models.endereco import Endereco
from atividade_aprendizagem.models.enums.estado_civil import EstadoCivil
from atividade_aprendizagem.models.enums.setor import Setor
from atividade_aprendizagem.models.enums.sexo import Sexo
from models.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float,crea: str) -> None:
        super().__init__(nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.crea = crea

    def __str__(self) -> str:
        return f"{super().__str__()}\nCrea: {self.crea}"
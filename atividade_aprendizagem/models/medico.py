from ..models.endereco import Endereco
from ..models.enums.estado_civil import EstadoCivil
from ..models.enums.setor import Setor
from ..models.enums.sexo import Sexo
from ..models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self,id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float,crm: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento, cpf, rg, matricula, setor, salario)
        self.crm = self._verificar_crm(crm)

    def _verificar_crm(self,crm):
        self._verificar_crm_vazio_invalido(crm)
        return crm

    def _verificar_crm_vazio_invalido(self,valor):
        if not valor.strip():
            raise TypeError("O CRM não pode ser vazio.")

    def __str__(self) -> str:
        return f"{super().__str__()}\nCrm: {self.crm}"
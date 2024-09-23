from ..models.endereco import Endereco
from ..models.enums.estado_civil import EstadoCivil
from ..models.enums.sexo import Sexo
from ..models.fisica import Fisica

class Cliente(Fisica):
    def __init__(self,id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str,protocoloAtendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return f"{super().__str__()}\nProtocolo de Atendimento: {self.protocoloAtendimento}"
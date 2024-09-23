from .pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil,dataNascimento: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento

    def __str__(self) -> str:
        return f"{super().__str__()}"
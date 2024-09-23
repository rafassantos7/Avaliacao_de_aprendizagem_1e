from abc import ABC, abstractmethod
from ..models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self,id: int,nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self._verificar_id(id)
        self.nome = self._verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def _verificar_nome(self,nome):
        if nome == "":
            raise ValueError("O nome não pode ser vazio")
        return nome

    def _verificar_id(self,id):
        if not isinstance (id, int): 
            raise TypeError("O id não pode conter letras.")
        return id
    
    @abstractmethod
    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}"
        )
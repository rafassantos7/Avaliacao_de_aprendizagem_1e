from ..models.endereco import Endereco
from ..models.juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str,produto: str) -> None:
        super().__init__(nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = produto

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nProduto: {self.produto}"
                )
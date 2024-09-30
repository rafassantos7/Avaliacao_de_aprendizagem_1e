from ..models.endereco import Endereco
from ..models.juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self,id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str,produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = self._verificar_produto_vazio_invalido(produto)

    def verificar_produto(self,produto):
        self._verificar_produto_vazio_invalido(produto)
        return produto

    def _verificar_produto_vazio_invalido(self,valor):
        if not valor.strip():
            raise TypeError("O produto não pode ser vazio.")
        
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nProduto: {self.produto}"
                )
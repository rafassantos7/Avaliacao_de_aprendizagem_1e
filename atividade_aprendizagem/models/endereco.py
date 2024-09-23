from models.enums.unidade_federativa import UnidadeFederativa

class Endereco:
    def __init__(self,logradouro: str, numero: str, complemento: str,cep: str,cidade: str,uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep 
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNumero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCep: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUf: {self.uf.nome}/{self.uf.sigla}"
        )
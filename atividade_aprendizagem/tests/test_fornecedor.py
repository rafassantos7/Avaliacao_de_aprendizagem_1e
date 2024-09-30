import pytest
from ..models.fornecedor import Fornecedor
from ..models.endereco import Endereco
from ..models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def criar_fornecedor():
    return Fornecedor(123,"Malu","40028922","maluzinha@gmail.com",
                 Endereco("Rua das pitanguinhas","152","Não sabe","478134","Salvador",UnidadeFederativa.BAHIA)
                 ,"123450001","1718763","Maquiagem")
                 

def test_nome_valido(criar_fornecedor):
    assert criar_fornecedor.nome == "Malu"

def test_alterar_nome_valido(criar_fornecedor):
    criar_fornecedor.nome = "Laura"
    assert criar_fornecedor.nome == "Laura"

def test_nome_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O nome não pode ser vazio"):
        Fornecedor(123,"","40028922","maluzinha@gmail.com",
                 Endereco("Rua das pitanguinhas","152","Não sabe","478134","Salvador",UnidadeFederativa.BAHIA)
                 ,"123450001","1718763","Maquiagem")
        
def test_id_invalida_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match="O id não pode conter letras."):
       Fornecedor("123","Malu","40028922","maluzinha@gmail.com",
                 Endereco("Rua das pitanguinhas","152","Não sabe","478134","Salvador",UnidadeFederativa.BAHIA)
                 ,"123450001","1718763","Maquiagem")
       
def test_produto_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O produto não pode ser vazio."):
        Fornecedor(123,"Malu","40028922","maluzinha@gmail.com",
                 Endereco("Rua das pitanguinhas","152","Não sabe","478134","Salvador",UnidadeFederativa.BAHIA)
                 ,"123450001","1718763","")

def test_email_invalido_retorna_mensagem_excessao():
    with pytest.raises(ValueError,match = "O email deve conter @."):
        Fornecedor(123,"Malu","40028922","maluzinhagmail.com",
                 Endereco("Rua das pitanguinhas","152","Não sabe","478134","Salvador",UnidadeFederativa.BAHIA)
                 ,"123450001","1718763","Maquiagem")
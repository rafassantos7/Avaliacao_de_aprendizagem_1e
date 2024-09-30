import pytest
from ..models.cliente import Cliente
from ..models.enums.estado_civil import EstadoCivil
from ..models.endereco import Endereco
from ..models.enums.sexo import Sexo
from ..models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def criar_cliente():
    return Cliente(777,"Rafael","40028922","rafael@gmail.com",
                   Endereco("Rua das garrafas","7","Proximo a rua da coca-cola","4342344","Salvador",UnidadeFederativa.BAHIA),
                   Sexo.MASCULINO,EstadoCivil.CASADO,"11/07/2001",32)

def test_nome_valido(criar_cliente):
    assert criar_cliente.nome == "Rafael"

def test_alterar_nome_valido(criar_cliente):
    criar_cliente.nome = "Vitor"
    assert criar_cliente.nome == "Vitor"

def test_nome_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O nome não pode ser vazio."):
        Cliente(777,"","40028922","rafael@gmail.com",
                   Endereco("Rua das garrafas","7","Proximo a rua da coca-cola","4342344","Salvador",UnidadeFederativa.BAHIA),
                   Sexo.MASCULINO,EstadoCivil.CASADO,"11/07/2001",32)

def test_id_invalida_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match="O id não pode conter letras."):
        Cliente("777","Rafael","40028922","rafael@gmail.com",
                   Endereco("Rua das garrafas","7","Proximo a rua da coca-cola","4342344","Salvador",UnidadeFederativa.BAHIA),
                   Sexo.MASCULINO,EstadoCivil.CASADO,"11/07/2001",32)



def test_tipo_protocolo_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O protocolo deve conter apenas números."):
        Cliente(777,"Rafael","40028922","rafael@gmail.com",
                   Endereco("Rua das garrafas","7","Proximo a rua da coca-cola","4342344","Salvador",UnidadeFederativa.BAHIA),
                   Sexo.MASCULINO,EstadoCivil.CASADO,"11/07/2001","32")


def test_email_invalido_retorna_mensagem_excessao():
    with pytest.raises(ValueError,match = "O email deve conter @."):
        Cliente(777,"Rafael","40028922","rafaelgmail.com",
                   Endereco("Rua das garrafas","7","Proximo a rua da coca-cola","4342344","Salvador",UnidadeFederativa.BAHIA),
                   Sexo.MASCULINO,EstadoCivil.CASADO,"11/07/2001",32)

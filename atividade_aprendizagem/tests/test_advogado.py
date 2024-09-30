import pytest
from ..models.advogado import Advogado
from ..models.enums.estado_civil import EstadoCivil
from ..models.endereco import Endereco
from ..models.enums.sexo import Sexo
from ..models.enums.setor import Setor
from ..models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def criar_advogado():
    return Advogado(555,"Patricia","1321-4242","patypatricinha@gmail.com",
                    Endereco("Rua das paty","111","Proximo ao shopping","1234098","São Paulo",UnidadeFederativa.SAO_PAULO,),
                    Sexo.FEMININO,EstadoCivil.CASADO,"18/11/1994","232323422","123464421","555777888",Setor.JURIDICO,8000.50,"000001")

def test_nome_valido(criar_advogado):
    assert criar_advogado.nome == "Patricia"

def test_alterar_nome_valido(criar_advogado):
    criar_advogado.nome = "Laura"
    assert criar_advogado.nome == "Laura"

def test_nome_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O nome não pode ser vazio"):
        Advogado(555,"","1321-4242","patypatricinha@gmail.com",
                    Endereco("Rua das paty","111","Proximo ao shopping","1234098","São Paulo",UnidadeFederativa.SAO_PAULO,),
                    Sexo.FEMININO,EstadoCivil.CASADO,"18/11/1994","232323422","123464421","555777888",Setor.JURIDICO,8000.50,"000001")

def test_id_invalida_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match="O id não pode conter letras."):
        Advogado("aaa","Patricia","1321-4242","patypatricinha@gmail.com",
                    Endereco("Rua das paty","111","Proximo ao shopping","1234098","São Paulo",UnidadeFederativa.SAO_PAULO,),
                    Sexo.FEMININO,EstadoCivil.CASADO,"18/11/1994","232323422","123464421","555777888",Setor.JURIDICO,8000.50,"000001")

def test_salario_negativo_retorna_mensagem_excessao():
    with pytest.raises(ValueError, match= "O salário não pode ser negativo."):
        Advogado(555,"Patricia","1321-4242","patypatricinha@gmail.com",
                    Endereco("Rua das paty","111","Proximo ao shopping","1234098","São Paulo",UnidadeFederativa.SAO_PAULO,),
                    Sexo.FEMININO,EstadoCivil.CASADO,"18/11/1994","232323422","123464421","555777888",Setor.JURIDICO,-8000.50,"000001")


def test_salario_tipo_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O salário deve ser em float."):
        Advogado(555,"Patricia","1321-4242","patypatricinha@gmail.com",
                    Endereco("Rua das paty","111","Proximo ao shopping","1234098","São Paulo",UnidadeFederativa.SAO_PAULO,),
                    Sexo.FEMININO,EstadoCivil.CASADO,"18/11/1994","232323422","123464421","555777888",Setor.JURIDICO,"8000.50","000001")

def test_oab_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O OAB não pode ser vazio."):
        Advogado(555,"Patricia","1321-4242","patypatricinha@gmail.com",
                    Endereco("Rua das paty","111","Proximo ao shopping","1234098","São Paulo",UnidadeFederativa.SAO_PAULO,),
                    Sexo.FEMININO,EstadoCivil.CASADO,"18/11/1994","232323422","123464421","555777888",Setor.JURIDICO,8000.50,"")


def test_email_invalido_retorna_mensagem_excessao():
    with pytest.raises(ValueError,match = "O email deve conter @."):
        Advogado(555,"Patricia","1321-4242","patypatricinhagmail.com",
                    Endereco("Rua das paty","111","Proximo ao shopping","1234098","São Paulo",UnidadeFederativa.SAO_PAULO,),
                    Sexo.FEMININO,EstadoCivil.CASADO,"18/11/1994","232323422","123464421","555777888",Setor.JURIDICO,8000.50,"")

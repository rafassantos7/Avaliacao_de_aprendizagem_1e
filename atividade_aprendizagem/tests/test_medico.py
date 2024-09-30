import pytest
from ..models.medico import Medico 
from ..models.enums.estado_civil import EstadoCivil
from ..models.endereco import Endereco
from ..models.enums.sexo import Sexo
from ..models.enums.setor import Setor
from ..models.enums.unidade_federativa import UnidadeFederativa


@pytest.fixture
def criar_medico():
    return Medico(777,"Pedro","7187984-9876","pedro000@gmail.com",
                  Endereco("Rua dos brasileiros","102","Proximo a rua dos paraguaios","4100000","São Paulo",UnidadeFederativa.SAO_PAULO),
                  Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"01/03/1975","48721598745","484321-897","8795464",Setor.SAUDE,10000.01,"654654")

def test_nome_valido(criar_medico):
    assert criar_medico.nome == "Pedro"

def test_alterar_nome_valido(criar_medico):
    criar_medico.nome = "Rodrigo"
    assert criar_medico.nome == "Rodrigo"

def test_nome_invalido_retorna_mensagem_excessao():
    with pytest.raises(ValueError, match= "O nome não pode ser vazio"):
        Medico(777,"","7187984-9876","pedro000@gmail.com",
                  Endereco("Rua dos brasileiros","102","Proximo a rua dos paraguaios","4100000","São Paulo",UnidadeFederativa.SAO_PAULO),
                  Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"01/03/1975","48721598745","484321-897","8795464",Setor.SAUDE,10000.01,"654654")


def test_id_invalida_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match="O id não pode conter letras."):
        Medico("777","Pedro","7187984-9876","pedro000@gmail.com",
                  Endereco("Rua dos brasileiros","102","Proximo a rua dos paraguaios","4100000","São Paulo",UnidadeFederativa.SAO_PAULO),
                  Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"01/03/1975","48721598745","484321-897","8795464",Setor.SAUDE,10000.01,"654654")
        
def test_salario_negativo_retorna_mensagem_excessao():
    with pytest.raises(ValueError, match= "O salário não pode ser negativo."):
        Medico(777,"Pedro","7187984-9876","pedro000@gmail.com",
                  Endereco("Rua dos brasileiros","102","Proximo a rua dos paraguaios","4100000","São Paulo",UnidadeFederativa.SAO_PAULO),
                  Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"01/03/1975","48721598745","484321-897","8795464",Setor.SAUDE,- 10000.01,"654654")


def test_salario_tipo_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O salário deve ser em float."):
        Medico(777,"Pedro","7187984-9876","pedro000@gmail.com",
                  Endereco("Rua dos brasileiros","102","Proximo a rua dos paraguaios","4100000","São Paulo",UnidadeFederativa.SAO_PAULO),
                  Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"01/03/1975","48721598745","484321-897","8795464",Setor.SAUDE,"10000.01","654654")


def test_salario_tipo_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O salário deve ser em float."):
        Medico(777,"Pedro","7187984-9876","pedro000@gmail.com",
                  Endereco("Rua dos brasileiros","102","Proximo a rua dos paraguaios","4100000","São Paulo",UnidadeFederativa.SAO_PAULO),
                  Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"01/03/1975","48721598745","484321-897","8795464",Setor.SAUDE,"10000.01","654654")

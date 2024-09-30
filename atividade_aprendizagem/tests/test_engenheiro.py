import pytest
from ..models.engenheiro import Engenheiro
from ..models.enums.estado_civil import EstadoCivil
from ..models.endereco import Endereco
from ..models.enums.sexo import Sexo
from ..models.enums.setor import Setor
from ..models.enums.unidade_federativa import UnidadeFederativa


@pytest.fixture
def criar_engenheiro():
    return Engenheiro(123, "Luis Sérgio" ,"21286428","luisinhorj@hotmail.com",
                         Endereco("Rua dos RJotinha","123","ap 02","4123500","Petropolis",UnidadeFederativa.RIO_DE_JANEIRO)
                         ,Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"08/06/1974","657124500","1642631","3845323846"
                         ,Setor.ENGENHARIA,20.000,"n sabemos")


def test_nome_valido(criar_engenheiro):
    assert criar_engenheiro.nome == "Luis Sérgio"

def test_alterar_nome_valido(criar_engenheiro):
    criar_engenheiro.nome = "Caio"
    assert criar_engenheiro.nome == "Caio"

def test_nome_invalido_retorna_mensagem_excessao():
    with pytest.raises(ValueError, match= "O nome não pode ser vazio"):
        Engenheiro(123,"","21286428","luisinhorj@hotmail.com",
                         Endereco("Rua dos RJotinha","123","ap 02","4123500","Petropolis",UnidadeFederativa.RIO_DE_JANEIRO)
                         ,Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"08/06/1974","657124500","1642631","3845323846"
                         ,Setor.ENGENHARIA,20.000,"n sabemos")

def test_id_invalida_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match="O id não pode conter letras."):
        Engenheiro("1234","Luis Sérgio","21286428","luisinhorj@hotmail.com",
                         Endereco("Rua dos RJotinha","123","ap 02","4123500","Petropolis",UnidadeFederativa.RIO_DE_JANEIRO)
                         ,Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"08/06/1974","657124500","1642631","3845323846"
                         ,Setor.ENGENHARIA,20.000,"n sabemos")

def test_salario_negativo_retorna_mensagem_excessao():
    with pytest.raises(ValueError, match= "O salário não pode ser negativo."):
        Engenheiro(1234,"Luis Sérgio","21286428","luisinhorj@hotmail.com",
                         Endereco("Rua dos RJotinha","123","ap 02","4123500","Petropolis",UnidadeFederativa.RIO_DE_JANEIRO)
                         ,Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"08/06/1974","657124500","1642631","3845323846"
                         ,Setor.ENGENHARIA, -20.000 ,"n sabemos")


def test_salario_tipo_invalido_retorna_mensagem_excessao():
    with pytest.raises(TypeError, match= "O salário deve ser em float."):
        Engenheiro(1234,"Luis Sérgio","21286428","luisinhorj@hotmail.com",
                         Endereco("Rua dos RJotinha","123","ap 02","4123500","Petropolis",UnidadeFederativa.RIO_DE_JANEIRO)
                         ,Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"08/06/1974","657124500","1642631","3845323846"
                         ,Setor.ENGENHARIA, "20000" ,"n sabemos")


import os
from models.endereco import Endereco
#from .models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import UnidadeFederativa    
from models.fornecedor import Fornecedor
from models.jobs.engenheiro import Engenheiro
from models.jobs.advogado import Advogado
from models.cliente import Cliente
from models.jobs.medico import Medico
from models.enums.estado_civil import EstadoCivil
from models.enums.setor import Setor


pessoa1 = Fornecedor("Malu","40028922","maluzinha@gmail.com",
                 Endereco("Rua das pitanguinhas","152","n sei","478134","Salvador",UnidadeFederativa.BAHIA)
                 ,"123450001","1718763","Maquiagem")


print(pessoa1)


engenheiro1 = Engenheiro("Luis Sérgio","21286428","luisinhocarequinha@hotmail.com",
                         Endereco("Rua dos RJotinha","123","ap 02","4123500","Petropolis",UnidadeFederativa.RIO_DE_JANEIRO)
                         ,Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"08/06/1974","657124500","1642631","3845323846",Setor.ENGENHARIA,"20.000","n sabemos")

print()
print(engenheiro1)
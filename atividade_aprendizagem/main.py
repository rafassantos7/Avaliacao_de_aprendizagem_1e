import os
from models.endereco import Endereco
#from .models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import UnidadeFederativa    
from models.fornecedor import Fornecedor
from models.engenheiro import Engenheiro
from models.advogado import Advogado
feom

pessoa1 = Fornecedor("Malu","40028922","maluzinha@gmail.com",
                 Endereco("Rua das pitanguinhas","152","n sei","478134","Salvador",UnidadeFederativa.BAHIA)
                 ,"123450001","1718763","Maquiagem")


print(pessoa1)
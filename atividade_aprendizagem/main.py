import os
from .models.engenheiro import Engenheiro
from .models.endereco import Endereco
from .models.fornecedor import Fornecedor
from .models.enums.unidade_federativa import UnidadeFederativa
from .models.enums.setor import Setor
from .models.enums.sexo import Sexo
from .models.enums.estado_civil import EstadoCivil



os.system("clear")
pessoa1 = Fornecedor(123,"Malu","40028922","maluzinha@gmail.com",
                 Endereco("Rua das pitanguinhas","152","Não sabe","478134","Salvador",UnidadeFederativa.BAHIA)
                 ,"123450001","1718763","Maquiagem")


print(pessoa1)


engenheiro1 = Engenheiro(234,"Luis Sérgio","21286428","luisinhocarequinha@hotmail.com",
                         Endereco("Rua dos RJotinha","123","ap 02","4123500","Petropolis",UnidadeFederativa.RIO_DE_JANEIRO)
                         ,Sexo.MASCULINO,EstadoCivil.DIVORCIADO,"08/06/1974","657124500","1642631","3845323846"
                         ,Setor.ENGENHARIA,20444.234,"Não sabemos")

print()
print(engenheiro1)
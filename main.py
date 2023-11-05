import pandas as pd
from classificar import Classificar

source_path = "src\Vendas.xlsx"

#Preciso separar os arquivos por categoria, como:
# - Faturamento dos produtos por loja (X)
# - Faturamento total dos produtos    (X)
# - Total por código de venda         (X)

classficador = Classificar(source_path, input("Digite a coluna pela qual você quer classificar o arquivo: "))

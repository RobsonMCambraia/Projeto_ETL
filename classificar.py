import pandas as pd
import os

class Classificar:
    def __init__(self, arquivo, coluna):
        self.coluna_escolhida = coluna
        self.arquivo_utilizado = arquivo
        
        self.faturamento()
        
    def faturamento(self):
        vendas_df = pd.read_excel(self.arquivo_utilizado)
        # Faturamento por loja
        lista_classificatoria = vendas_df[self.coluna_escolhida].drop_duplicates().tolist()
        
        for i in lista_classificatoria:
            index = lista_classificatoria.index(i)
            arquivo_ref = vendas_df.loc[vendas_df[self.coluna_escolhida] == lista_classificatoria[index]]
            arquivo_ref.to_excel(f'src/{i}.xlsx')
            
        return "operação finalizada com sucesso!"
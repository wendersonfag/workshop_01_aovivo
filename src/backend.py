import pandas as pd
from contrato import Vendas
import os

def process_excel(upload_file):
    try:
        df = pd.read_excel(upload_file)
        erros = []
        # verificar se há colunas extras no DataFrame
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no Excel: {','.join(extra_cols)}"
        
        # validar cada linha com o schema escolhido
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                erros.append(f"Erro na linha {index + 2}: {e}")
        
        # retorna tanto o resultado da validação, os erros, quanto o DataFrame
        return True, erros
    
    except Exception as e:
        # se houver exceção, retorna o erro em um DataFrame vazio
        return pd.DataFrame(), f"Erro inesperado: {str(e)}"
        

import pandas as pd
import re

def limpar_dados(lista_dados):
    if not lista_dados:
        return pd.DataFrame()

    df = pd.DataFrame(lista_dados)

    def tratar_preco(preco_str):
        if isinstance(preco_str, (int, float)):
            return float(preco_str)
        # Remove tudo que não é número ou vírgula
        apenas_numeros = re.sub(r'[^\d,]', '', str(preco_str))
        if apenas_numeros:
            return float(apenas_numeros.replace(',', '.'))
        return 0.0

    # Aplica a limpeza nas duas colunas
    df['Preço Atual'] = df['Preço Atual Bruto'].apply(tratar_preco)
    df['Preço Antigo'] = df['Preço Antigo Bruto'].apply(tratar_preco)
    
    # Organiza a ordem final das colunas
    colunas_finais = [
        "Data Coleta", "Loja", "Produto", 
        "Preço Antigo", "Preço Atual", # Deixamos lado a lado
        "URL"
    ]
    
    # Retorna apenas colunas que existem (segurança)
    return df[[c for c in colunas_finais if c in df.columns]]
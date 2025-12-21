import streamlit as st
import pandas as pd
import os
from config import ARQUIVO_SAIDA

st.title("📊 Dashboard de Preços")

st.markdown("Visualize o histórico de preços coletados.")

if os.path.exists(ARQUIVO_SAIDA):
    df = pd.read_excel(ARQUIVO_SAIDA)
    st.dataframe(df)

    # Gráfico simples de preços
    if 'Preço Atual' in df.columns and 'Produto' in df.columns:
        st.subheader("Preços Atuais por Produto")
        st.bar_chart(df.groupby('Produto')['Preço Atual'].last())
else:
    st.warning("Arquivo de dados não encontrado. Execute o scraper primeiro.")
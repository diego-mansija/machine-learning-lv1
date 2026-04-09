import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Configuração de interface profissional
st.set_page_config(page_title="Predição de Demanda", layout="wide")
st.title("Sistema Preditivo: Inteligência de Vendas")

@st.cache_data
def load_and_process():
    df = pd.read_csv('./data/vendas.csv')
    df['Data'] = pd.to_datetime(df['Data'])
    # Agrupamento mensal para série temporal
    df_mensal = df.resample('ME', on='Data')['Quantidade'].sum().reset_index()
    df_mensal['Mes_Ordinal'] = np.arange(len(df_mensal))
    return df_mensal

df_ml = load_and_process()

# 1. Treinamento do Modelo (Machine Learning)
X = df_ml[['Mes_Ordinal']]
y = df_ml['Quantidade']
modelo = LinearRegression()
modelo.fit(X, y)

# 2. Interface de Predição
st.sidebar.header("Parâmetros de Projeção")
meses_futuros = st.sidebar.slider("Meses para prever:", 1, 12, 3)

# Cálculo da previsão
proximos_meses = np.array([[len(df_ml) + i] for i in range(meses_futuros)])
previsoes = modelo.predict(proximos_meses)

# 3. Exibição de Resultados
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tendência de Demanda")
    fig, ax = plt.subplots()
    ax.scatter(df_ml['Data'], y, color='blue', label='Histórico')
    
    # Datas futuras para o gráfico
    datas_futuras = pd.date_range(df_ml['Data'].max(), periods=meses_futuros + 1, freq='ME')[1:]
    ax.plot(datas_futuras, previsoes, color='red', linestyle='--', marker='o', label='Predição')
    
    plt.xticks(rotation=45)
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Métricas de Projeção")
    total_previsto = previsoes.sum()
    st.metric("Volume Total Previsto", f"{int(total_previsto)} unidades")
    st.write("O modelo utiliza Regressão Linear para identificar a tendência de crescimento baseada no histórico de vendas.")
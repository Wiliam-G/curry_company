from plotly import express as px
import streamlit as st
from utils import data_cleaning
from utils.graficos_visao_empresa import *
from utils import side_bar

df = pd.read_csv("../dataset/train.csv")

# ===================
# LIMPEZA DOS DADOS
# ===================
df1 = data_cleaning.limpar_dados(df.copy())

st.set_page_config(
    page_title="Visão Empresa",
    page_icon="📊",
    layout="wide")

# ====================================================
# SIDEBAR
# ====================================================

df1 = side_bar.side_bar(df1)

# ====================================================
# LAYOUT DO STREAMLIT
# ====================================================

st.header("Marketplace - Visão Empresa")

tab1, tab2, tab3 = st.tabs(["Visão Gerencial", "Visão Tática", "Visão Geográfica"])

with tab1:
    with st.container():
        st.header("Orders by day")
        fig = pedidos_por_dia(df1)    
        st.plotly_chart(fig, use_container_width = True)

    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.header("Order traffic share")
            fig = distribuicao_por_trafego(df1)
            st.plotly_chart(fig, use_container_width = True)
        with col2:
            st.header("Traffic order city")
            fig = pedidos_por_cidade_trafego(df1)
            st.plotly_chart(fig, use_container_width=True)

with tab2:
    with st.container():
        st.header("Pedidos por semana do ano")
        fig = pedidos_semana(df1)
        st.plotly_chart(fig, use_container_width = True)

    with st.container():
        st.header("Pedidos por entregador por semana")
        fig = pedidos_entregador_semana(df1)
        st.plotly_chart(fig, use_container_width = True)

with tab3:
    mapa(df1)
    













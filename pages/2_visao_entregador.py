import pandas as pd
from plotly import express as px
from haversine import haversine
import streamlit as st
from utils import data_cleaning
from utils import side_bar
from utils.graficos_visao_entregadores import *

df = pd.read_csv("../dataset/train.csv")

df1 = data_cleaning.limpar_dados(df.copy())

# ====================================================
# SIDEBAR
# ====================================================

st.set_page_config(
    page_title="Visão Entregador",
    page_icon="🚚",
    layout="wide"
)

df1 = side_bar.side_bar(df1)

# ====================================================
# LAYOUT DO STREAMLIT
# ====================================================

tab1, tab2, tab3 = st.tabs(["Visão Entregadores", "_", "_"])

with tab1:
    with st.container():
        st.title("Overall metrics")
        col1, col2, col3, col4 = st.columns(4, gap = "large")
        with col1:
            max = df1.loc[:, "Delivery_person_Age"].max()
            col1.metric("Maior idade", max)
            
        with col2:
            min = df1.loc[:, "Delivery_person_Age"].min()
            col2.metric("Menor idade", min)
        with col3:
            melhor = df1.loc[:, "Vehicle_condition"].max()
            col3.metric("Melhor condição de veículo", melhor)
        with col4:
            pior = df1.loc[:, "Vehicle_condition"].min()
            col4.metric("Pior condição de veículo", pior)

    with st.container():
        st.markdown("""---""")
        st.title("Avaliações")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("##### Avaliação média por entregador")
            media_por_entregador = df1.loc[:, ["Delivery_person_ID", "Delivery_person_Ratings"]].groupby("Delivery_person_ID").mean().reset_index()
            st.dataframe(media_por_entregador)

        with col2:
            st.markdown("##### Avaliação média por trânsito")
            media = avaliacao_media_transito(df1)
            st.dataframe(media)

            st.markdown("##### Avaliação média por clima")
            media = avaliacao_media_clima(df1)
            st.dataframe(media)

    with st.container():
        st.markdown("""---""")
        st.title("Velocidade de entrega")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### Top entregadores mais rápidos")
            top_entregadores_mais_rapidos = entregadores_mais_rapidos(df1)    
            st.dataframe (top_entregadores_mais_rapidos)
        with col2:
            st.markdown("##### Top entregadores mais lentos")
            top_entregadores_mais_lentos = entregadores_mais_lentos(df1)
            st.dataframe(top_entregadores_mais_lentos)
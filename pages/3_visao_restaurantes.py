import pandas as pd
import numpy as np
from plotly import express as px
import folium
import streamlit as st
from streamlit_folium import folium_static
from utils import side_bar
from utils import data_cleaning
from utils.graficos_visao_restaurantes import *

df = pd.read_csv("../dataset/train.csv")

df1 = data_cleaning.limpar_dados(df.copy())

# ====================================================
# SIDEBAR
# ====================================================
st.set_page_config(
    page_title="Visão Restaurantes",
    page_icon="🍟",
    layout="wide"
)

st.header("Marketplace - Visão entregadores")

df1 = side_bar.side_bar(df1)

# ====================================================
# LAYOUT DO STREAMLIT
# ====================================================

tab1, tab2, tab3 = st.tabs(["Visão restaurantes", "_", "_"])

with tab1:
    with st.container():
        st.title("Overal metrics")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            entregadores = df1["Delivery_person_ID"].nunique()
            col1.metric("Entregadores únicos", entregadores)
        with col2:
            distancia_media = distancia_media_restaurante_entregas(df1)
            col2.metric("Distância média", distancia_media)
        with col3:
            tempo_medio_entrega_com_festival = tempo_medio_entrega_festival(df1)
            col3.metric("Tempo médio c/ festival", tempo_medio_entrega_com_festival)
        with col4:
            desvio_padrao_festival = desvio_padrao_entregas_festival(df1)
            col4.metric("Desvio padrão do tempo c/ festival", desvio_padrao_festival)
        with col5:
            tempo_medio_entregas = tempo_medio_entregas_sem_festival(df1)
            col5.metric("Tempo médio s/ festival", tempo_medio_entregas)
        with col6:
            desvio_padrao = desvio_padrao_sem_festival(df1)
            col6.metric("Desvio padrão do tempo s/ festival", desvio_padrao)

    with st.container():
            st.markdown("""---""")
            col1, col2 = st.columns(2)
            with col1:         
                st.markdown("##### Distribuição do tempo por cidade (gráfico com intervalos)")
                fig = tempo_entrega_por_cidade(df1)
                st.plotly_chart(fig)
                
            with col2:
                st.markdown("##### Tempo médio por tipo de entrega (tabela)")
                tempo_medio_cidade_trafego = tempo_medio_entregas_por_cidade_trafego(df1)
                st.dataframe(tempo_medio_cidade_trafego)
                
    with st.container():
        st.markdown("""---""")
        st.markdown("### Distribuição do tempo")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("##### Distribuição média da distância por cidade (pizza)")
            fig = distribuicao_distancia_media_cidade(df1)
            st.plotly_chart(fig)

        with col2:
            st.markdown("##### Tempo médio por cidade e tipo de tráfego")
            fig = tempo_medio_tipo_entrega(df1)
            st.plotly_chart(fig)
            


        
import streamlit as st
from datetime import datetime
from plotly import express as px

def side_bar(df1, filter = True):
    
    st.sidebar.markdown("# Curry Company")
    st.sidebar.markdown("## Fastest Delivery in Town")
    st.sidebar.markdown("""---""")
    st.sidebar.markdown("## Selecione uma data limite")
    
    if filter == True:
    
        data_slider = st.sidebar.slider(
            "Até qual valor?",
            value=datetime(2022, 4, 13),  # Valor padrão
            min_value=datetime(2022, 2, 11),
            max_value=datetime(2022, 4, 6),
            format="DD-MM-YYYY"
        )
        
        
        print(df1.head())
        
        st.sidebar.markdown("""---""")
        
        traffic = ["Low", "Medium", "High", "Jam"]
        
        traffic_options = st.sidebar.multiselect(
            "Quais as condições do trânsito?",
            traffic,
            default = traffic
        )
        
        st.sidebar.markdown("""---""")
        
        st.sidebar.markdown("### Powered by Comunidade DS")
        
        # Filtro de data
        
        rows = df1["Order_Date"] <= data_slider
        df1 = df1.loc[rows, :]
        
        # Filtro de trânsito
        rows = df1["Road_traffic_density"].isin(traffic_options)
        df1 = df1.loc[rows, :]
    
        return df1

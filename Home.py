import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🎲"
)

st.sidebar.markdown("# Cury Company")
st.sidebar.markdown("## Fastest Delivery in Town")
st.sidebar.markdown("""---""")
st.sidebar.markdown("## Selecione uma data limite")

st.sidebar.markdown("""---""")

st.sidebar.markdown("### Powered by Comunidade DS")

st.write("# Curry company growth dashboard")
st.markdown(
    """
    Growth Dashboard foi construído para acompanhar as métricas de crescimento dos entregadores e restaurantes.
    ### Como utilizar esse Growth Dashboard?
    - Visão Empresa:
        - Visão Gerencial: Métricas gerais de comportamento.
        - Visão Tática: Indicadores semanais de crescimento.
        - Visão Estratégica: Insights de geolocalização.
    - Visão Entregadores: 
        - Acompanhamento dos indicadores semanais de crescimento.
    - Visão Restaurantes:
        - Indicadores semanais de crescimento dos restaurantes.
    ### Ask for help
    - Time de data analytics do Discord
        -@.Scarh
    """
)


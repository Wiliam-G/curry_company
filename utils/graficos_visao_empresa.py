from plotly import express as px
import pandas as pd
import folium
from streamlit_folium import folium_static

def pedidos_por_dia(df):
    df1 = df
    # contagem de pedidos por dia
    df_aux = df1.loc[:, ["ID", "Order_Date"]].groupby("Order_Date").count().reset_index()
        
    fig = px.bar(df_aux, x="Order_Date", y="ID")
    return fig

def distribuicao_por_trafego(df):
    df1 = df
    df_aux = df1.loc[:, ["ID", "Road_traffic_density"]].groupby("Road_traffic_density").count().reset_index()
    df_aux["percentual_entregas"] = df_aux["ID"] / df_aux["ID"].sum()
    fig = px.pie(df_aux, values="percentual_entregas", names="Road_traffic_density")
    return fig


def pedidos_por_cidade_trafego(df):
    df1 = df
    df_aux = df1.loc[:, ["ID", "City", "Road_traffic_density"]].groupby(["City", "Road_traffic_density"]).count().reset_index()
    
    fig =px.scatter(df_aux, x="City", y="Road_traffic_density", size="ID")
    return fig


def pedidos_semana(df):
    df1 = df
    df1["week_of_year"] = df1["Order_Date"].dt.isocalendar().week
    df_aux = df1.loc[:, ["ID", "week_of_year"]].groupby("week_of_year").count().reset_index()
            
    fig = px.line(df_aux, x="week_of_year", y="ID")
    return fig


def pedidos_entregador_semana(df):
    df1 = df
    df_aux1 = df1.loc[:, ["ID", "week_of_year"]].groupby("week_of_year").count().reset_index()
    df_aux2 = df1.loc[:, ["Delivery_person_ID", "week_of_year"]].groupby("week_of_year").nunique().reset_index()
    df_aux = pd.merge(df_aux1, df_aux2, how="inner")
    df_aux["order_by_delivery"] = df_aux["ID"] / df_aux["Delivery_person_ID"]
            
    fig = px.line(df_aux, x="week_of_year", y="order_by_delivery")
    return fig


def mapa(df):
    df1 = df
    df_aux = df1.loc[:, ["City", "Road_traffic_density", "Delivery_location_latitude", "Delivery_location_longitude"]].groupby(["City", "Road_traffic_density"]).median().reset_index()
    map = folium.Map()
    for index, location_info in df_aux.iterrows():
        folium.Marker([location_info["Delivery_location_latitude"], location_info["Delivery_location_longitude"]]).add_to(map)
    folium_static(map, width = 1024, height = 600)
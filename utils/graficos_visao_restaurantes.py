from haversine import haversine
import numpy as np
from plotly import graph_objects as go
from plotly import express as px

def distancia_media_restaurante_entregas(df):
    df1 = df
    cols = ["Restaurant_latitude", "Restaurant_longitude", "Delivery_location_latitude", "Delivery_location_longitude"]
    df1["Distance"] = df1.loc[:, cols].apply(lambda x: 
                    haversine(
                    (x["Restaurant_latitude"], x["Restaurant_longitude"]), 
                    (x["Delivery_location_latitude"], x["Delivery_location_longitude"]) ), axis=1)
    
    media = np.round(df1["Distance"].mean(), 2)
    return media

def tempo_medio_entrega_festival(df):
    df1 = df
    rows = df1.loc[df1["Festival"] == "Yes"]
    df_aux = rows.loc[:, ["Time_taken(min)", "Festival"]].groupby("Festival").agg({"Time_taken(min)": ["mean", "std"]})
    df_aux.columns = ["time_mean", "time_std_deviation"]
    tempo_medio_festival = np.round(df_aux.loc[:, "time_mean"], 2)
    return tempo_medio_festival

def desvio_padrao_entregas_festival(df):
    df1 = df
    rows = df1.loc[df1["Festival"] == "Yes"]
    df_aux = rows.loc[:, ["Time_taken(min)", "Festival"]].groupby("Festival").agg({"Time_taken(min)": ["mean", "std"]})
    df_aux.columns = ["time_mean", "time_std_deviation"]
    desvio_padrao = np.round(df_aux.loc[:, "time_std_deviation"], 2)
    return desvio_padrao

def tempo_medio_entregas_sem_festival(df):
    df1 = df
    rows = df1.loc[df1["Festival"] == "No"]
    df_aux = rows.loc[:, ["Time_taken(min)", "Festival"]].groupby("Festival").agg({"Time_taken(min)": ["mean", "std"]})
    df_aux.columns = ["time_mean", "time_std_deviation"]
    tempo_medio = np.round(df_aux.loc[:, "time_mean"], 2)
    return tempo_medio

def desvio_padrao_sem_festival(df):
    df1 = df
    rows = df1.loc[df1["Festival"] == "No"]
    df_aux = rows.loc[:, ["Time_taken(min)", "Festival"]].groupby("Festival").agg({"Time_taken(min)": ["mean", "std"]})
    df_aux.columns = ["time_mean", "time_std_deviation"]
    desvio_padrao = np.round(df_aux.loc[:, "time_std_deviation"], 2)
    return desvio_padrao

def tempo_entrega_por_cidade(df):
    df1 = df
    df_aux = df1.loc[:, ["Time_taken(min)", "City"]].groupby("City").agg({"Time_taken(min)": ["mean", "std"]})
    df_aux.columns = ["City_mean", "City_std"]
    df_aux = df_aux.reset_index()
                    
    fig = go.Figure()
    fig.add_trace(go.Bar(name = "Control", x = df_aux["City"], y = df_aux["City_mean"], error_y = dict(type = "data", array = df_aux["City_std"])))
    fig.update_layout(barmode = "group")
    return fig

def tempo_medio_entregas_por_cidade_trafego(df):
    df1 = df
    df_aux = df1.loc[:, ["Time_taken(min)", "City", "Type_of_order"]].groupby(["City", "Type_of_order"]).agg({"Time_taken(min)": ["mean", "std"]})
    df_aux.columns = ["City_mean", "City_std"]
    df_aux = df_aux.reset_index()
    return df_aux

def distribuicao_distancia_media_cidade(df):
    df1 = df
    cols = ["Restaurant_latitude", "Restaurant_longitude", "Delivery_location_latitude", "Delivery_location_longitude"]
    df1["Distance"] = df1.loc[:, cols].apply(lambda x: 
                    haversine(
                        (x["Restaurant_latitude"], x["Restaurant_longitude"]), 
                        (x["Delivery_location_latitude"], x["Delivery_location_longitude"]) ), axis=1)
        
    avg_distance = df1.loc[:, ["City", "Distance"]].groupby("City").mean().reset_index()
                
    fig = go.Figure(data = [go.Pie(labels = avg_distance["City"], values = avg_distance["Distance"], pull = [0,0.1,0])])
    return fig

def tempo_medio_tipo_entrega(df):
    df1 = df
    df_aux = df1.loc[:, ["Time_taken(min)", "City", "Road_traffic_density"]].groupby(["City", "Road_traffic_density"]).agg({"Time_taken(min)": ["mean", "std"]})
    df_aux.columns = ["City_mean", "City_std"]
    df_aux = df_aux.reset_index()
            
    fig = px.sunburst(df_aux, path = ["City", "Road_traffic_density"], values = "City_mean", color = "City_std", color_continuous_scale = "RdBu", color_continuous_midpoint = np.average(df_aux["City_std"]))
    return fig
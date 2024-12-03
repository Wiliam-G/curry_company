import pandas as pd

def avaliacao_media_transito(df):
    df1 = df
    media = df1.loc[:, ["Delivery_person_Ratings", "Road_traffic_density"]].groupby("Road_traffic_density").agg({"Delivery_person_Ratings": ["mean", "std"]})
    media.columns = ["Delivery_mean", "Delivery_std"]
    media.reset_index()
    return media

def avaliacao_media_clima(df):
    df1 = df
    media = df1.loc[:, ["Delivery_person_Ratings", "Weatherconditions"]].groupby("Weatherconditions").agg({"Delivery_person_Ratings": ["mean", "std"]})
    media.columns = ["Delivery_mean", "Delivery_std"]
    media.reset_index()
    return media

def entregadores_mais_rapidos(df):
    df1 = df
    df2 = (df1.loc[:, ["Delivery_person_ID", "City", "Time_taken(min)"]]
                .groupby(["City", "Delivery_person_ID"])
                .min()
                .sort_values(["City", "Time_taken(min)"], ascending = True)
                .reset_index())
                
    df_aux1 = df2.loc[df2["City"] == "Metropolitian"].head(10)
    df_aux2 = df2.loc[df2["City"] == "Urban"].head(10)
    df_aux3 = df2.loc[df2["City"] == "Semi-Urban"].head(10)
    
    df3 = pd.concat([df_aux1, df_aux2, df_aux3] ).reset_index(drop = True)
    return df3

def entregadores_mais_lentos(df):
    df1 = df
    df2 = (df1.loc[:, ["Delivery_person_ID", "City", "Time_taken(min)"]]
                .groupby(["City", "Delivery_person_ID"])
                .max()
                .sort_values(["City", "Time_taken(min)"], ascending = False)
                .reset_index())
                
    df_aux1 = df2.loc[df2["City"] == "Metropolitian"].head(10)
    df_aux2 = df2.loc[df2["City"] == "Urban"].head(10)
    df_aux3 = df2.loc[df2["City"] == "Semi-Urban"].head(10)
                
    df3 = pd.concat([df_aux1, df_aux2, df_aux3] ).reset_index(drop = True)
    return df3
import pandas as pd

def limpar_dados(df):
    '''Realiza a limpeza dos dados'''
    
    df1 = df
    # remove espaços vazios no final das colunas de texto
    df1["ID"] = df1.loc[:, "ID"].str.strip()
    df1["Road_traffic_density"] = df1.loc[:, "Road_traffic_density"].str.strip()
    df1["Type_of_vehicle"] = df1.loc[:, "Type_of_vehicle"].str.strip()
    df1["Type_of_order"] = df1.loc[:, "Type_of_order"].str.strip()
    df1["City"] = df1.loc[:, "City"].str.strip()
    df1["Festival"] = df1.loc[:, "Festival"].str.strip()
    
    # remove linhas em que a coluna Delivery_person_Age é NaN
    df1 = df1.loc[df1["Delivery_person_Age"] != "NaN ", :]
    # altera o tipo da coluna Delivery_person_Age para int
    df1["Delivery_person_Age"] = df1["Delivery_person_Age"].astype(int)
    
    # remove linhas em que a coluna multiple_deliveries é NaN
    df1 = df1.loc[df1["multiple_deliveries"] != "NaN "]
    # # altera o tipo da coluna Multiple_deliveries para int
    df1["multiple_deliveries"] = df1["multiple_deliveries"].astype(int)
    
    # remove linhas em que a coluna Road_traffic_density é NaN
    df1 = df1.loc[df1["Road_traffic_density"] != "NaN"]
    
    # remove linhas em que a coluna City é NaN
    df1 = df1.loc[df1["City"] != "NaN"]
    
    # altera o tipo da coluna Delivery_person_Ratings para float
    df1["Delivery_person_Ratings"] = df1["Delivery_person_Ratings"].astype(float)
    
    # altera a coluna Order_date para datetime no formato dd/mm/yyyy
    df1["Order_Date"] = pd.to_datetime(df1["Order_Date"], format="%d-%m-%Y")
    
    # remove a parte de texto da coluna Time_taken(min), mantendo só o número e converte para int
    df1["Time_taken(min)"] = df1["Time_taken(min)"].str.split().str[1]
    df1["Time_taken(min)"] = df1.loc[:, "Time_taken(min)"].astype(int)
    
    # reseta o index
    df1 = df1.reset_index(drop = True)

    return df1
import pandas as pd
import requests
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import csv

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense,Dropout,GRU

anos = 2021
#2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020

def obtener_datos_anos(ano):
    url = f'https://www.usagold.com/daily-gold-price-history/?ddYears={ano}'

    # This restores the same behavior as before.
    response = requests.get(url, headers=
        {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        })
    # tabla_1 = pd.read_html(response.text, attrs = {'id': 'pricehistorytable'})
    
    tabla = pd.read_html(response.text, attrs = {'id': 'pricehistorytable'}, header=0)
    tabla_1 = tabla[0]
    
    return tabla_1


def guardar_datos():
    # todos_anos_precio = [obtener_datos_anos(ano) for ano in anos]
    todos_anos_precio = []
    # for ano in anos:
    #     datos_ano = obtener_datos_anos(ano)
    #     todos_anos_precio.append(datos_ano)
    
    pd.set_option('display.max_rows', None)
    df = obtener_datos_anos(anos)
    # print(df.size)
    # print(df.shape)
    # print(list(df.columns))
    df = df['Closing Price']
    df.columns = ["Precio_cierre"]
    df =  df.iloc[::-1]

    
    

    df.to_csv("df_precio_2021.csv", index=False)

        # todos_anos_precio.append(datos_ano)


    # df = pd.DataFrame(todos_anos_precio)
    # pd.set_option('display.max_rows', None)

    
    print("*************DF LEIDO***********************")
    print("********************************************")



    # texto = df.to_string(index=False)
    # print(texto)
    # print(type(texto))
    # with open("archivo.txt", "w") as archivo:
    #     archivo.write(texto)

    # df.to_csv("df_precio_2021.csv", index=False)

def preparar_datos():
    with open('archivo.txt', 'r') as file:
    # Leer las líneas del archivo de texto
        lines = file.readlines()
        listas = []
        
    # Abrir el archivo CSV en modo de escritura
    with open('archivo.csv', 'w', newline='') as file:
    # Crear un objeto escritor CSV
        writer = csv.writer(file)

    for i in lines:
        # listas.append (i[23:])

        writer.writerow(i[23:])
            
    return
    

    # scaler = MinMaxScaler(feature_range=(0,1))
    # scaled_data = scaler.fit_transform(hist['Close'].values.reshape(-1,1))


guardar_datos()

# preparar_datos()




print("***************************  fin ***********************")

# todos_anos_precio = [obtener_datos_anos(ano) for ano in anos]
# todos_anos_precio = []
#     for ano in anos:
#         datos_ano = obtener_datos_anos(ano)
#         todos_anos_precio.append(datos_ano)
import pandas as pd
import requests
import csv
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return'Servidor - Web Scraping - Modelo Oro!'

if __name__=='__main__':
    app.run(debug=True, port=4000)


anos = 2021

def obtener_datos_anos(ano):
    url = f'https://www.usagold.com/daily-gold-price-history/?ddYears={ano}'

    response = requests.get(url, headers=
        {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        })
    
    tabla = pd.read_html(response.text, attrs = {'id': 'pricehistorytable'}, header=0)
    tabla_1 = tabla[0]
    
    return tabla_1

def guardar_datos():
    todos_anos_precio = []
    pd.set_option('display.max_rows', None)
    df = obtener_datos_anos(anos)
    df = df['Closing Price']
    df.columns = ["Precio_cierre"]
    df =  df.iloc[::-1]

    df.to_csv("df_precio_2021.csv", index=False)

    
    print("*************DF LEIDO***********************")
    print("********************************************")


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


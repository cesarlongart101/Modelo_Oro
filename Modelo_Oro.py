import pandas as pd
import requests


anos = [2022]
#2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020


def obtener_datos_anos(ano):
    

    url = f'https://www.usagold.com/daily-gold-price-history/?ddYears={ano}'

    # This restores the same behavior as before.
    response = requests.get(url, headers=
        {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        })
    
    tabla_1 = pd.read_html(response.text, attrs = {'id': 'pricehistorytable'})
    

    return tabla_1


# todos_anos_precio = [obtener_datos_anos(ano) for ano in anos]
# df = pd.DataFrame(todos_anos_precio)

# pd.set_option('display.max_rows', None)

# df.to_csv("df_precio_2022.csv")

print("***************************  fin ***********************")


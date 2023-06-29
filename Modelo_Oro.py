import pandas as pd
#from bs4 import BeautifulSoup
import requests


anos = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

url = 'https://www.usagold.com/daily-gold-price-history/?ddYears=2000'

# This restores the same behavior as before.
response = requests.get(url, headers=
    {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
#print(response.text)
tabla_1 = pd.read_html(response.text, attrs = {'id': 'pricehistorytable'})
print(len(tabla_1))

print(type(tabla_1))
print(tabla_1)
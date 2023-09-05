import pandas as pd
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/obtener_datos_ano')
def obtener_datos_ano():
    url = f'https://www.usagold.com/daily-gold-price-history/?ddYears=2022'

    response = requests.get(url, headers=
        {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        })
    
    tabla = pd.read_html(response.text, attrs = {'id': 'pricehistorytable'}, header=0)
    tabla_1 = tabla[0]
    json_data = tabla_1.to_dict(orient='records')
    return jsonify(json_data)


if __name__=='__main__':
    app.run(debug=True, port=4000)



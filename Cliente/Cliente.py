import requests
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np


url = 'http://localhost:4000/obtener_datos_ano'
response = requests.get(url)
fecha_inicio = "25 Jan 2022"
day_counter = 60
counter = 0
encontrada = False
selected_data = []

# Respuesta de ENDPOINT, cargar y filtrar los datos
if response.status_code == 200:
    data = response.json()
    data.reverse()
    for dict in data:
        if day_counter > counter:
            if encontrada:
                selected_data.append(dict)
                counter = counter + 1
            elif dict["date"] == fecha_inicio:
                selected_data.append(dict)
                encontrada = True
                counter = counter + 1
        else:
            break
else:
    print('Error al hacer la solicitud')

# print(selected_data)

# Convertir lista en Dataframe
df = pd.json_normalize(selected_data, sep='_')

# Escalar precio a rango entre 0 y 1
scaler = MinMaxScaler(feature_range=(0,1))

scaled_data = scaler.fit_transform(df['Closing Price'].values.reshape(-1,1))

print(scaled_data)
# x_train = []
# y_train = []

# for x in range(scaled_data):
#   x_train.append(scaled_data[x-day_counter:x,0])
#   y_train.append(scaled_data[x,0])

# x_train,y_train = np.array(x_train),np.array(y_train)
# x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

# x_train.shape



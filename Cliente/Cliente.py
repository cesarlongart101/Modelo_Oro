import requests
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,GRU
import matplotlib.pyplot as plt


url = 'http://localhost:4000/obtener_datos_ano'
response = requests.get(url)
fecha_inicio = "31 Jan 2022"
day_counter = 60

# Respuesta de ENDPOINT, cargar y filtrar los datos
if response.status_code == 200:
    data = response.json()
    data.reverse()
else:
    print('Error al hacer la solicitud')

# print(len(data))

# Convertir lista en Dataframe
# df = pd.json_normalize(selected_data, sep='_')
df = pd.json_normalize(data, sep='_')
df.drop(261, inplace=True)

# Escalar precio a rango entre 0 y 1
scaler = MinMaxScaler(feature_range=(0,1))

scaled_data = scaler.fit_transform(df['Closing Price'].values.reshape(-1,1))
# print(scaled_data)

x_train = []
y_train = []

for x in range(day_counter, len(scaled_data)):
  x_train.append(scaled_data[x-day_counter:x,0])
  y_train.append(scaled_data[x,0])


#Convierte las listas x_train y y_train en arrays 
x_train,y_train = np.array(x_train),np.array(y_train)
#Le agrega una tercera dimension al arrays porque asi lo pide la red neuroanal 
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

# print(x_train.shape)

# Construyendo el modelo
model = Sequential()

model.add(GRU(units=50,return_sequences = True, input_shape=(x_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(GRU(units=50,return_sequences = True))
model.add(Dropout(0.2))
model.add(GRU(units=50))
model.add(Dropout(0.1))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(x_train,y_train,epochs=25,batch_size=32)

# Cargar los datos del test
hist_test = df
actual_prices = hist_test['Closing Price'].values



total_dataset = pd.concat((df['Closing Price'],hist_test['Closing Price']),axis=0)
model_inputs = total_dataset[len(total_dataset)-len(hist_test)-day_counter:].values
model_inputs = scaler.transform(model_inputs.reshape(-1,1))

# Hacer las predicciones
x_test = []

for x in range(day_counter,len(model_inputs)):
  x_test.append(model_inputs[x-day_counter:x,0])

x_test = np.array(x_test)
x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))

predicted_prices = model.predict(x_test)
predicted_prices = scaler.inverse_transform(predicted_prices)

# Graficos precio real vs precio de las predicciones
plt.plot(actual_prices,color="black",label=f"Precio real del ORO")
plt.plot(predicted_prices,color="blue",label=f"Predicción precio del ORO")
plt.legend()
plt.show()

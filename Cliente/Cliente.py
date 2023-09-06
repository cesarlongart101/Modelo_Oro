import requests

url = 'http://localhost:4000/obtener_datos_ano'
response = requests.get(url)
fecha_inicio = "31 Jan 2022"
day_counter = 2
counter = 0
encontrada = False
selected_data = []

if response.status_code == 200:
    data = response.json() 
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

print(selected_data)




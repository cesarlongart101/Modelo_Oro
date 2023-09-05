import requests

url = 'http://localhost:4000/obtener_datos_ano'
response = requests.get(url)

# if response.status_code == 200:
#     data = response.json() 
#     print(data) 
# else:
#     print('Error al hacer la solicitud')


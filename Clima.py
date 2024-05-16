import requests

def obtener_clima(ciudad, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={ciudad}&lang=es"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        hora = datos['location']['localtime']
        descripcion = datos['current']['condition']['text']
        temperatura = datos['current']['temp_c']
        humedad = datos['current']['humidity']
        viento = datos['current']['wind_kph']
        presion = datos['current']['pressure_mb']
        visibilidad = datos['current']['vis_km']
        sensacion_termica = datos['current']['feelslike_c']
        
        print(f"Clima en {ciudad}:")
        print(f"Hora local: {hora}")
        print(f"Descripción: {descripcion}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Humedad: {humedad}%")
        print(f"Velocidad del viento: {viento} kph")
        print(f"Presión atmosférica: {presion} mb")
        print(f"Visibilidad: {visibilidad} km")
        print(f"Sensación térmica: {sensacion_termica}°C")
    else:
        print("No se pudo obtener el clima. Por favor, verifica el nombre de la ciudad y tu clave de API.")

if __name__ == "__main__":
    ciudad = input("Introduce el nombre de la ciudad: ")
    api_key = "bc6b1b3784f245d6a3100948240904"
    obtener_clima(ciudad, api_key)

from tkinter import *
import requests

#41237cee69fed118dd395d074c59dbaa
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def mostrar_respuesta(clima):
    try:
        nombre_ciudad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]

        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp)) + "°C"
        descripcion["text"] = desc
    except:
        ciudad["text"] = "Intenta nuevamente" 

def clima_json(ciudad):
    try:
        API_key = "41237cee69fed118dd395d074c59dbaa"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID" : API_key, "q": ciudad, "units": "metric", "lang": "es"}
        response = requests.get(URL, params = parametros)
        clima = response.json()
        mostrar_respuesta(clima)
    except:
        print("Error") 
        
   
ventana = Tk()
ventana.geometry("400x400")

texto_ciudad = Entry(ventana, font = ("Courrier", 20, "normal"), justify = "center")
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text = "Obtener Temperatura", font = ("Courrier", 20, "normal"), command = lambda: clima_json(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font = ("courier", 20, "normal"))
ciudad.pack(padx = 20, pady = 20)

temperatura = Label(font = ("courier", 50, "normal"))
temperatura.pack(padx = 10, pady = 10)

descripcion = Label(font = ("courier", 20, "normal"))
descripcion.pack(padx = 10, pady = 10)

ventana.mainloop()
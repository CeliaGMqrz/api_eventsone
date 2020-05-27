#Programa en python que muestra todos los eventos segun código del pais, con el artista o los artistas, la fecha, el lugar y la url para comprar la entrada

#Para ello necesitas autentificarte con la API key.
# Esta API utiliza la respuesta json.

#Vamos a usar variables de entorno para guardar nuestra key.
# Deremos exportar la clave de nuestra cuenta en una variable de entorno desde la terminal:
# export key ="**************************"

#Lo primero es importar la librería requests
import requests
#Importamos la libreria json
import json
#Importar la librería os que va leer nuestra variable de entorno
import os

#Importar las fechas
from datetime import datetime

#Guardamos la url base
url_base="https://app.ticketmaster.com/discovery/v2/"

#En una variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["apikey"]

#Función que recibe el código del país y devuelve el nombre, la sala, la dirección, la fecha y la url

def mostrar_evento (codigo_pais):
    #Creamos el diccionario con los parámetros necesarios
    payload = {'apikey':key,'countryCode':codigo_pais}
    #Guardamos la petición en una variable(urlbase + diccionario con parametros)
    r=requests.get(url_base+'events',params=payload)
    #Inicializamos las listas necesarias
    nombres=[]
    fechas=[]
    horas=[]
    salas=[]
    direccion=[]
    ciudades=[]
    urls=[]
    #Comprobamos que la peticion es correcta
    if r.status_code == 200:
        #Guardamos el contenido en json
        contenido = r.json()
        #Añadimos la información a cada lista
        for elem in contenido["_embedded"]["events"]:
            nombres.append(elem["name"])
            urls.append(elem["url"])
            fechas.append(elem["dates"]["start"]["localDate"])
            horas.append(elem["dates"]["start"]["localTime"])
            salas.append(elem["_embedded"]["venues"][0]["name"])
            direccion.append(elem["_embedded"]["venues"][0]["address"]["line1"])
            ciudades.append(elem["_embedded"]["venues"][0]["state"]["name"])
        filtro=[nombres,fechas,horas,salas,direccion,ciudades,urls]
        return filtro 

codpais=input("Introduce el código del pais: ")
for nombre,fecha,hora,sala,direc,ciudad,url in zip((mostrar_evento(codpais)[0]),(mostrar_evento(codpais)[1]),(mostrar_evento(codpais)[2]),(mostrar_evento(codpais)[3]),(mostrar_evento(codpais)[4]),(mostrar_evento(codpais)[5]),(mostrar_evento(codpais)[6])):
    fecha_cambiada = datetime.strptime(fecha, '%Y-%m-%d')
    fecha_str = datetime.strftime(fecha_cambiada, '%d/%m/%Y')
    print("\n\nNOMBRE:",nombre,"\nURL COMPRAR ENTRADA:",url,"\nFECHA:",fecha_str,"\nHORA:",hora,"\nSALA:",sala,"\nDIRECCIÓN:",direc,"\nCIUDAD:",ciudad) 

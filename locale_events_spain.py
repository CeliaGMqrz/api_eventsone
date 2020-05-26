#Programa en python que devuelve la sala y el lugar donde se celebran eventos internacionales en España.

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

#Guardamos la url base
url_base="https://app.ticketmaster.com/discovery/v2/"

#En una variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["apikey"]
#Guardamos en una variable el código del país, en esta caso España
code='ES'
#Vamos a crear un diccionario que guarde nuestros parámetros
payload = {'apikey':key,'countryCode':code}

#Hacemos la petición, guardandola en una variable r, añadiendo los parametros que necesitamos usando params e indicando el diccionario creado previamente.
r=requests.get(url_base+'venues.json',params=payload)

#Para asegurarnos que no hay errores consultamos el estado de la petición.
#Inicializamos las listas que nos hacen falta
salas=[]
lugares=[]
if r.status_code == 200:
    #Guardamos el contenido en una variable leido por json.
    doc = r.json()
    for lugar in doc["_embedded"]["venues"]:
        salas.append(lugar["name"])
        lugares.append(lugar["state"]["name"])
    filtro=[salas,lugares]
    
    for sala,lugar in zip(filtro[0],filtro[1]):
        print("SALA: ",lugar,"\nLUGAR:",sala)


#Importamos la librería requests
import requests
#Importamos la libreria json
import json
#Importar la librería os que va leer nuestra variable de entorno
import os
#Guardamos la url base
url_base="https://api.themoviedb.org/3/"
#En una variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["api_key"]
#Guardamos en una variable el código del país, en esta caso Inglaterra
code='EN'
#Vamos a crear un diccionario que guarde nuestros parámetros
payload = {'api_key':key,"languaje":'en-EN'}
#Pedimos el título de una película por teclado y nos muestra el json de TheMovieDB
pelicula = input("Introduce el nombre de la pelicula: ")
#Construimos la url con los parámetros
url = url_base+'search/movie'+'?query='+pelicula
r=requests.get(url,params=payload)
#Guardamos en una variable el contenido de la respuesta
if r.status_code == 200:
    doc=r.json()
    #Mostramos el contenido de la respuesta
    print(json.dumps(doc, indent=4, sort_keys=True))
else:
    print ("Error")
    print (r.status_code)
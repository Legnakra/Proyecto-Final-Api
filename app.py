#Importar herramientas necesarias de flask
from flask import Flask, render_template, abort,request
import requests

#Importar librería os para emplear environ
import os

#Importar json para lectura de MSX.json
import json

#Variable app por flask
app = Flask(__name__)

#Guardamos la url base
url_base="https://api.themoviedb.org/3/"
url_base2="https://ghibliapi.herokuapp.com/"

#En una variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["api_key"]

#Guardamos en una variable el código del país, en esta caso Inglaterra
code='EN'

#Vamos a crear un diccionario que guarde nuestros parámetros
payload = {'api_key':key,'countryCode':code}

#Definir ruta de inicio
@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

#Definir ruta categorias
@app.route('/peliculas',methods=["GET"])
def peliculas():
	r= requests.get(url_base2+"films")
	if r.status_code==200:
		lista_peliculas=[]
		for pelicula in r.json():
			lista_peliculas.append(pelicula.get('title'))
		print (lista_peliculas)
		return render_template("peliculas.html",peliculas=lista_peliculas)
	else:
		abort(404)
port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=False) 
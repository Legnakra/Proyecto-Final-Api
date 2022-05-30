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
@app.route('/peliculas',methods=["GET","POST"])
def peliculas():
    lista_peliculas=[]
    directores=[]
    directores.append("")
    r= requests.get(url_base2+"films")
    if r.status_code==200:
        for i in r.json():
            if i.get('director') not in directores:
                directores.append(i.get('director'))
        directores.sort()
    if request.method=="GET":
        return render_template("peliculas.html",directores=directores)
    else:
        nombre=request.form.get('title')
        director=request.form.get('director')
        if r.status_code==200:
            for i in r.json():
                if (nombre == "" or i['title'].startswith(nombre)):
                    lista_peliculas.append(i.get('title'))
            return render_template("peliculas.html", pelicula=lista_peliculas, director=director, nombre=nombre, directores=directores)
        return render_template("peliculas.html",directores=directores,director=director,nombre=nombre,pelicula=lista_peliculas)

#Definir ruta detalle
@app.route('/detalles/<title>',methods=["GET"])
def detalle(title):
	title=title.replace("_"," ")
	r= requests.get(url_base2+"films")
	if r.status_code==200:
		for pelicula in r.json():
			if pelicula.get('title')==title:
				titulo=pelicula.get('title')
				tit_original=pelicula.get('original_title')
				poster=pelicula.get('image')
				romanised=pelicula.get('original_title_romanised')
				release_date=pelicula.get('release_date')
				director=pelicula.get('director')
				producer=pelicula.get('producer')
				duracion=pelicula.get('running_time')
				puntuacion=pelicula.get('rt_score')
				descripcion=pelicula.get('description')
				return render_template("detalle.html",pelicula=pelicula,original=tit_original,poster=poster,titulo=titulo,romanised=romanised,release_date=release_date,director=director,producer=producer,duracion=duracion,puntuacion=puntuacion,descripcion=descripcion)
		else:
			abort(404)
			
port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=False) 
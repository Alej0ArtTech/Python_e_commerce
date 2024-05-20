from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from django.template import Context, Template
from django.shortcuts import render


# def saludar(request):
#     return HttpResponse(" Hola Django :)")
# def otra_vista(request):
#     return HttpResponse("<h1> Hola Django :)</h1>")

# def nombre(request, nombre:str, apellido: str):
#     nombre = nombre.capitalize()
#     apellido = apellido.capitalize()
#     return HttpResponse(f"<h1> Hola {nombre} {apellido} </h1>")


# def probando_template(request):
#     datos = {
#         "saludo": "¡Bienvenido a Django!",
#         "autor": "Coderhouse",
#     }
#     print(datos)
#     return render(request, "template1.html", datos)

# def probando_template(request):
#     mi_html = open("./templates/template1.html", encoding="UTF-8")
#     mi_template = Template(mi_html.read())
#     mi_html.close()
#     mi_contexto = Context({"saludo": "¡Bienvenido", "autor": "Coderhause"})
#     mi_documento = mi_template.render(mi_contexto)
#     return HttpResponse(mi_documento)


# def probando_template(request):
#     datos = {
#         "saludo": "¡Bienvenido a Django!",
#         "autor": "Coderhouse",
#     }
#     print(datos)
#     return render(request, "template1.html", datos)


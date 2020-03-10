from django.http import HttpResponse
from django.template import Template, Context

def saludo(request): #primera vista
	doc_externo = open("C:/Users/TOSHIBA/Desktop/Osmar/proyectos django/primero/primero/plantillas/plantilla.html")
	plantilla = Template(doc_externo.read())
	doc_externo.close()
	ctx = Context()
	documento = plantilla.render(ctx)

	return HttpResponse(documento)

def despedida(request): #segunda vista
	return HttpResponse("Adios a todos")
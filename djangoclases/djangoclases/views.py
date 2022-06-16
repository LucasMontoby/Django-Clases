from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse 

def saludo(request):
    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br> Ah entendimos esto, no era tan dificil!!")


def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto =f"Hoy es dia: <br> {dia}"
    
    return HttpResponse(documentoDeTexto)


def template(self):
    
    miHtml = open("C:/Users/monto/OneDrive/Escritorio/DjangoClases/djangoclases/djangoclases/plantilla/template.html")
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)
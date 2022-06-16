from datetime import datetime
from django.http import HttpResponse 
from django.template import Context
from django.template import Template


def saludo(request):
    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br> Ah entendimos esto, no era tan dificil!!")


def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto =f"Hoy es dia: <br> {dia}"
    
    return HttpResponse(documentoDeTexto)


def template(self):
    
    miHtml = open(r'C:/Users/monto/OneDrive/Escritorio/DjangoClases/djangoclases/djangoclases/plantilla/template.html', 'r')
    
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)
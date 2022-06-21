from datetime import datetime
from unittest import loader
from django.http import HttpResponse 
from django.template import Context
from django.template import Template, loader


def saludo(request):
    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br> Ah entendimos esto, no era tan dificil!!")


def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto =f"Hoy es dia: <br> {dia}"
    
    return HttpResponse(documentoDeTexto)

# V1
#def template(request):
    
#    miHtml = open(r'C:/Users/monto/OneDrive/Escritorio/DjangoClases/djangoclases/djangoclases/plantilla/template.html', 'r')
    
#    plantilla = Template(miHtml.read())
    
#    miHtml.close()
    
#    miContexto = Context()
    
#    documento = plantilla.render(miContexto)
    
#    return HttpResponse(documento)

    
# V2
def template(request):
    
    plantilla = loader.get_template("template.html")

    nombre = "Momia"
    
    render1 = plantilla.render({"nombre" : nombre})
    
    return HttpResponse(render1)
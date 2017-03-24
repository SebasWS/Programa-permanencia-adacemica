from django.http import HttpResponse
from django.template import loader
#from django.shortcuts import render

# Create your views here.
def Pagina_Principal(entrada):
    template=loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,entrada))

def Ingreso_Estudiante(entrada):
    template=loader.get_template('single-post.html')
    context={}
    return HttpResponse(template.render(context,entrada))

def Ingreso_Evaluador(entrada):
    template=loader.get_template('single-project.html')
    context={}
    return HttpResponse(template.render(context,entrada))



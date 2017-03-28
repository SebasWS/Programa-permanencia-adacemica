from django.http import HttpResponse
from django.template import loader
import random
import matplotlib.pyplot as plt
import os
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

def Encuesta(entrada):
    template=loader.get_template('gracias.html')
    dato=entrada.POST
    filelist = [ f for f in os.listdir("Aplicacion/templates/imagenes/") if f.endswith(".png") ]
    for f in filelist:
        os.remove("Aplicacion/templates/imagenes/"+f)
    lista1=[]
    lista2=[]
    lista3=[]
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)

    x=range(0,4,1)
    #y1=[lista1[3],lista2[3],lista3[3],int(dato["radio3"])]
    probabilidad=(0.2*float(dato["radio28"]))+(0.025*float(dato["radio1"]))+(0.025*float(dato["radio3"]))+(0.025*float(dato["radio4"]))+(0.025*float(dato["radio7"]))+(0.05*float(dato["radio10"]))+(0.1*float(dato["radio11"]))+(0.05*float(dato["radio12"]))+(0.05*float(dato["radio15"]))+(0.05*float(dato["radio16"]))+(0.05*float(dato["radio26"]))+(0.01944*float(dato["radio"]))+(0.01944*float(dato["radio2"]))+(0.01944*float(dato["radio5"]))+(0.01944*float(dato["radio6"]))+(0.01944*float(dato["radio8"]))+(0.01944*float(dato["radio9"]))+(0.01944*float(dato["radio13"]))+(0.01944*float(dato["radio14"]))+(0.01944*float(dato["radio17"]))+(0.01944*float(dato["radio18"]))+(0.01944*float(dato["radio19"]))+(0.01944*float(dato["radio20"]))+(0.01944*float(dato["radio21"]))+(0.01944*float(dato["radio22"]))+(0.01944*float(dato["radio23"]))+(0.01944*float(dato["radio24"]))+(0.01944*float(dato["radio25"]))+(0.01944*float(dato["radio27"]))
    print(probabilidad)
    yprob=[lista1[0],lista2[0],lista3[0],probabilidad]

    print(dato)
    plt.plot(x,yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('variable')
    plt.show()
    plt.savefig('Aplicacion/templates/imagenes/figure0.png')
    return HttpResponse(template.render(dato,entrada))





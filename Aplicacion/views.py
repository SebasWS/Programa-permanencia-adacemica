# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
import random
import matplotlib
matplotlib.use('Agg')
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

def Resultados(entrada):
    template=loader.get_template('resultados.html')
    context={}
    return HttpResponse(template.render(context,entrada))

def terminosycondiciones(entrada):
    template=loader.get_template('tyc.html')
    context={}
    return HttpResponse(template.render(context,entrada))

def Encuesta(entrada):
    filelist = [f for f in os.listdir("Aplicacion/static/imagenes/") if f.endswith(".png")]
    for f in filelist:
        os.remove("Aplicacion/static/imagenes/" + f)
    template=loader.get_template('gracias.html')
    dato=entrada.POST
    lista1=[]
    lista2=[]
    lista3=[]

    x=range(0,4,1)
    #grafica1: probabilidad
    for i in range(0,29,1):
        random1 = random.randrange(0, 100, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(0, 100, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(0, 100, 1)
        lista3.insert(i,random3)
    probabilidad=(0.03*float(dato["radio28"]))+(0.025*float(dato["radio1"]))+(0.025*float(dato["radio3"]))+(0.025*float(dato["radio4"]))+(0.025*float(dato["radio7"]))+(0.05*float(dato["radio10"]))+(0.1*float(dato["radio11"]))+(0.025*float(dato["radio12"]))+(0.05*float(dato["radio15"]))+(0.05*float(dato["radio16"]))+(0.05*float(dato["radio26"]))+(0.01944*float(dato["radio"]))+(0.01944*float(dato["radio2"]))+(0.01944*float(dato["radio5"]))+(0.01944*float(dato["radio6"]))+(0.01944*float(dato["radio8"]))+(0.01944*float(dato["radio9"]))+(0.01944*float(dato["radio13"]))+(0.01944*float(dato["radio14"]))+(0.01944*float(dato["radio17"]))+(0.01944*float(dato["radio18"]))+(0.01944*float(dato["radio19"]))+(0.01944*float(dato["radio20"]))+(0.01944*float(dato["radio21"]))+(0.01944*float(dato["radio22"]))+(0.01944*float(dato["radio23"]))+(0.01944*float(dato["radio24"]))+(0.01944*float(dato["radio25"]))+(0.01944*float(dato["radio27"]))+(0.03*float(dato["radio29"]))+(0.02*float(dato["radio30"]))++(0.02*float(dato["radio31"]))+(0.02*float(dato["radio32"]))+(0.02*float(dato["radio33"]))+(0.02*float(dato["radio34"]))+(0.02*float(dato["radio35"]))+(0.02*float(dato["radio36"]))+(0.02*float(dato["radio37"]))
    probabilidad=(-20*probabilidad)+100
    yprob=[lista1[0],lista2[0],lista3[0],probabilidad]
    plt.plot(x,yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Probabilidad de desercion (en %)')
    plt.title('Probabilidad de desercion del estudiante en el tiempo')
    plt.text(0.95, 0.01, 'Probabilidad actual de desercion: '+str(probabilidad),
            verticalalignment='bottom', horizontalalignment='left',
            color='red', fontsize=10)
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/probabilidad de desercion.png')
    plt.cla()
    #grafica2:perseverancia
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob=[lista1[0],lista2[0],lista3[0],int(dato["radio"])]
    plt.plot(x,yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Perseverancia caracteristica del individuo (medido de 0 a 5)')
    plt.title('Perseverancia caracteristica del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f1.png')
    plt.cla()
    #grafica3:expectativas de exito
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio1"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Expectativas de exito del individuo (medido de 0 a 5)')
    plt.title('Expectativas de exito del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f2.png')
    plt.cla()
    #grafica4:habilidad para estudiar
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio2"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Facilidad de aprendizaje (medido de 0 a 5)')
    plt.title('Facilidad de aprendizaje en el individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f3.png')
    plt.cla()
    #grafica5:ambiente familiar
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio3"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Ambiente familiar (medido de 0 a 5)')
    plt.title('Ambiente familiar del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f4.png')
    plt.cla()
    #grafica6:situacion en la universidad
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio4"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Situacion actual en la universidad (medido de 0 a 5)')
    plt.title('Situacion actual del individuo en la universidad')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f5.png')
    plt.cla()
    #grafica7:satisfaccion con el sistema academico
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio5"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Satisfaccion con el sistema academico (medido de 0 a 5)')
    plt.title('Sastisfaccion con el sistema academico del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f6.png')
    plt.cla()
    #grafica8:calificacion de la division de recreacion y deporte de la universidad
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio6"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Calificacion de la division de recreacion y deporte (medido de 0 a 5)')
    plt.title('Calificacion de la division de recreacion y deporte')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f7.png')
    plt.cla()
    #grafica9:calificacion de la calidad de la ensenanza en la universidad
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio7"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Calificacion de la ensenanza en la universidad (medido de 0 a 5)')
    plt.title('Calificacion de la ensenanza en la universidad')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f8.png')
    plt.cla()
    #grafica10:calificacion de la calidad de los docentes universitarios
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio8"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Calificacion de la calidad de los docentes universitarios (medido de 0 a 5)')
    plt.title('Calificacion de la calidad de los docentes segun el individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f9.png')
    plt.cla()
    #grafica11:disponibilidad de recursos
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio9"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Disponibilidad de recursos academicos (medido de 0 a 5)')
    plt.title('Disponibilidad de recursos academicos segun el individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f10.png')
    plt.cla()
    #grafica12:relacion costo beneficio
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio10"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Relacion costo-beneficio(medido de 0 a 5)')
    plt.title('Relacion costo-beneficio segun el individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f11.png')
    plt.cla()
    #grafica13:situacion economica
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio11"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Situacion economica (medido de 0 a 5)')
    plt.title('Situacion economica del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f12.png')
    plt.cla()
    #grafica14:nivel educativo de los padres
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio12"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Nivel educativo de los padres (medido de 0 a 5)')
    plt.title('Nivel educativo de los padres del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f13.png')
    plt.cla()
    #grafica15:adaptacion al ambiente universitario
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio13"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Adaptacion al ambiente universitario (medido de 0 a 5)')
    plt.title('Adaptacion al ambiente universitario del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f14.png')
    plt.cla()
    #grafica16:Desempeno academico
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio14"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Desempeno academico (medido de 0 a 5)')
    plt.title('Desempeno academico del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f15.png')
    plt.cla()
    #grafica17:compatibilidad entre horario y actividades extracurriculares
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio15"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Compatibilidad entre horaria (medido de 0 a 5)')
    plt.title('Compatibilidad entre horario y actividades extracurriculares del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f16.png')
    plt.cla()
    #grafica18:satisfaccion con la carrera elegida
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio16"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Satisfaccion con la carrera elegida(medido de 0 a 5)')
    plt.title('Satisfaccion del individuo con la carrera que eligio')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f17.png')
    plt.cla()
    #grafica19:nivel academico del colegio
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio17"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Nivel academico del colegio (medido de 0 a 5)')
    plt.title('Nivel academico del colegio del que salio el individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f18.png')
    plt.cla()
    #grafica20:calidad del proyecto academico
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio18"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Calidad del proyecto academico escogido (medido de 0 a 5)')
    plt.title('Calidad del proyecto academico escogido por el individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f19.png')
    plt.cla()
    #grafica21:resultados de la prueba saber
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio19"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Resultado promedio en las pruebas saber (medido de 0 a 5)')
    plt.title('Resultado promedio en las pruebas saber del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f20.png')
    plt.cla()
    #grafica22:servicios de financiamiento con los que cuenta el individuo
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio20"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Facilidad de financiamiento (medido de 0 a 5)')
    plt.title('Facilidad de financiamiento del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f21.png')
    plt.cla()
    #grafica23:situacion de orden publico
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio21"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Situacion de orden publico en la universidad (medido de 0 a 5)')
    plt.title('Situacion de orden publico en la universidad segun el individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f22.png')
    plt.cla()
    #grafica24:interaccion entre docentes y estudiantes
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio22"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Interaccion entre docentes y estudiantes(medido de 0 a 5)')
    plt.title('Interaccion entre docentes y estudiantes en la universidad')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f23.png')
    plt.cla()
    #grafica25:apoyo academico que ofrece el programa
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio23"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Apoyo academico que ofrece el programa (medido de 0 a 5)')
    plt.title('Apoyo academico que ofrece el programa del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f24.png')
    plt.cla()
    #grafica26:apoyo psicologico que ofrece la universidad
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio24"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Apoyo psicologico que ofrece la universidad (medido de 0 a 5)')
    plt.title('Apoyo psicologico que ofrece la universidad')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f25.png')
    plt.cla()
    #grafica27:situacion laboral del individuo
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio25"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Situacion economica (medido de 0 a 5)')
    plt.title('Situacion economica del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f26.png')
    plt.cla()
    # grafica28:situacion laboral de los padres
    for i in range(0, 29, 1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i, random1)

    for i in range(0, 29, 1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i, random1)

    for i in range(0, 29, 1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i, random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio26"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Situacion laboral de los padres (medido de 0 a 5)')
    plt.title('Situacion laboral de los padres del individuo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f27.png')
    plt.cla()
    #grafica29:dependencia economica a los padres o un tercero
    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista1.insert(i,random1)

    for i in range(0,29,1):
        random1 = random.randrange(1, 5, 1)
        lista2.insert(i,random1)

    for i in range(0,29,1):
        random3 = random.randrange(1, 5, 1)
        lista3.insert(i,random3)
    yprob = [lista1[0], lista2[0], lista3[0], int(dato["radio27"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Dependencia economica a los padres o a un tercero (medido de 0 a 5)')
    plt.title('Dependencia economica a los padres o a un tercero')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f28.png')
    plt.cla()
    #grafica30:Consumo de sustancias psicoactivas

    yprob = [5, 5, 5, int(dato["radio28"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Consumo de sustancias psicoactivas (no=5 a si=0)')
    plt.title('Consumo de sustancias psicoactivas')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f29.png')
    plt.cla()
    # grafica31:Existencia de embarazo

    yprob = [5, 5, 5, int(dato["radio29"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Existencia de embarazo (no=5 a si=0)')
    plt.title('Existencia de embarazo')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f30.png')
    plt.cla()
    # grafica32:Existencia de estado depresivo en el pasado

    yprob = [5, 5, 5, int(dato["radio30"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Conducta depresiva en el pasado (no=5 a si=0)')
    plt.title('Existencia de conductas depresivas en el pasado')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f31.png')
    plt.cla()
    # grafica33:Intento de suicidio en el pasado

    yprob = [5, 5, 5, int(dato["radio31"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Intento de suicidio en el pasado (no=5 a si=0)')
    plt.title('Existencia de intentos de suicidio en el pasado')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f32.png')
    plt.cla()
    # grafica34:Preocupaciones que afectan el rendimiento academico

    yprob = [5, 5, 5, int(dato["radio32"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Preocupaciones en general (no=5 a si=0)')
    plt.title('Preocupaciones que afectan el rendimiento academico')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f33.png')
    plt.cla()
    # grafica35:Existencia de depresion en la actualidad

    yprob = [5, 5, 5, int(dato["radio33"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Existencia de depresion en la actualidad (no=5 a si=0)')
    plt.title('Existencia de depresion en la actualidad')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f34.png')
    plt.cla()
    # grafica36:Ideas suicidas en el ultimo ano

    yprob = [5, 5, 5, int(dato["radio34"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Ideas suicidas en el ultimo ano (no=5 a si=0)')
    plt.title('Ideas suicidas en el ultimo ano')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f35.png')
    plt.cla()
    # grafica37:Intento de suicidio alguna vez en la vida

    yprob = [5, 5, 5, int(dato["radio35"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Intento de suicidio alguna vez en la vida (no=5 a si=0)')
    plt.title('Intento de suicidio alguna vez en la vida')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f36.png')
    plt.cla()
    # grafica38:Acoso sexual en el ambiente familiar

    yprob = [5, 5, 5, int(dato["radio36"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Acoso sexual en el ambiente familiar (no=5 a si=0)')
    plt.title('Acoso secual en el ambiente familiar')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f37.png')
    plt.cla()
    # grafica39:Acoso sexual en el ambiente univeristario

    yprob = [5, 5, 5, int(dato["radio36"])]
    plt.plot(x, yprob)
    plt.xlabel('Tiempo(en semestres)')
    plt.ylabel('Acoso sexual en el ambiente universitario (no=5 a si=0)')
    plt.title('Acoso secual en el ambiente universitario')
    plt.show()
    plt.savefig('Aplicacion/static/imagenes/f38.png')
    plt.cla()
    return HttpResponse(template.render(dato,entrada))





from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.Pagina_Principal, name='pagina1'),
    url(r'^Ingreso_estudiante/$', views.Ingreso_Estudiante, name='pagina2'),
    url(r'^Ingreso_evaluador/$', views.Ingreso_Evaluador, name='pagina3')
]

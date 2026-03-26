"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from registro import views as views_registro #Se coloca as para no confuncir el mismo nombre de la carpeta views/inicio
from django.conf import settings

urlpatterns = [
    #           
    path('admin/', admin.site.urls),
    #         nombre la     nombre de  
    #          carpeta      la funcion
    path('', views_registro.registros, name='principal'),
    path('contacto/',views_registro.contacto,name='contacto'),
    path('yio/',views.yio,name='yio'),
    path('formulario/',views_registro.formulario,name='Formulario'),
    path('ejemplo/',views.ejemplo,name='ejemplo'),
    path('registrar/',views_registro.resgistrar,name="Registrar"),
    path('comentarios/',views_registro.comentarios,name="Comentarios"),
    path('Eliminar/<int:id>/',views_registro.eliminarComentarioContacto,name='Eliminar'),
    path('Editar/<int:id>/',views_registro.editarComentarioContacto,name='Editar'),
    path('Consultar/<int:id>/',views_registro.consultarComentarioIndividual,name='Consultar'),
    path('consultas1',views_registro.consultar1, name='Consultas'),
    path('consultas2',views_registro.consultar2, name='Consultas'),
    path('consultas3',views_registro.consultar3, name='Consultas'),
    path('consultas4',views_registro.consultar4, name='Consultas'),
    path('consultas5',views_registro.consultar5, name='Consultas'),
    path('consultas6',views_registro.consultar6, name='Consultas'),
    path('consultas7',views_registro.consultar7, name='Consultas'),
    path('subir',views_registro.archivos, name='Subir'),
    path('consultasSQL', views_registro.consultarSQL, name='sql'),
    path('seguridad',views.seguridad, name='seguridad'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
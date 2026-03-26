from django.shortcuts import get_object_or_404, render
from .models import Alumnos, ComentarioContacto, Archivos
from .forms import ComentarioContactoForm, FormArchivos
from django.shortcuts import get_list_or_404
import datetime
from django.contrib import messages


# Create your views here.
def registros (request):
    alumnos=Alumnos.objects.all() #all -> recuperrar tosos los objetos del modelo (resgistros de la tabla alumnos)
    return render(request,'registro/principal.html',{'8A':alumnos} )
#Indicamos el lugar donde se renderizá el resultado de esta vista y enviamos la lista de alumnos recuperamos

def resgistrar(request):
    if request.method == 'POST':
        form= ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #Inserta
            comentario = ComentarioContacto.objects.all()
        return render(request,"registro/comentarios.html",{'comentarios':comentario})
    form= ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(render, 'registro/formulario.html', {'form': form})

def formulario (request):
    return render(request, "registro/formulario.html")
    #Indicamos el lugar donde se renderizará el resultado de esta vista

def contacto (request):
    return render(request,"registro/contacto.html")
#Indicamos el lugar donde se renderizará el resultado de esta vista

def comentarios (request):
    comentario = ComentarioContacto.objects.all()
    return render(request,"registro/comentarios.html",{'comentarios':comentario})

def eliminarComentarioContacto(request, id,
        confirmacion='registro/confirmarEliminacion.html'):
        comentario = get_list_or_404(ComentarioContacto, id=id)
        if request.method=='POST':
                comentario[0].delete()
                comentarios=ComentarioContacto.objects.all()
                return render(request,"registro/comentarios.html",
                        {'comentarios':comentarios})
                                
        return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
     comentario=ComentarioContacto.objects.get (id=id)
     #GET permite establecer una condición a la consulta y recupera el objetos.
     #del modelo que cumple la condición (registro de la tabla ComentariosContacto)
     #Get se emplea cuando se sabe que hay un objeto que coincide con su 
     #consulta
     return render(request, "registro/formEditarComentario.html",
                   {'comentarios':comentario})
    #Indicamos el lugar donde se renderrizará el resultado de esta vista 
    #y enviamos la vista de comentarios recuperados.

def editarComentarioContacto(request, id):
     comentario=get_object_or_404(ComentarioContacto, id=id)
     form= ComentarioContactoForm (request.POST, instance=comentario)
     #Referenciamos que el elemento del formulario pertenece al comentario ya existente
     if form.is_valid():
          form.save() #SI el registro ya existente, se modifica
          comentario= ComentarioContacto.objects.all()
          return render (request, "registro/comentarios.html", {'comentarios':comentario})
     return render(request, "registro/formEditarComentario.html", {'comentario': comentario})

def consultar1(request):
     alumnos=Alumnos.objects.filter(carrera='TI')
     #Consulta una sola condicion
     return render(request, "registro/consultas.html",{'8A':alumnos})

def consultar2(request):
     alumnos=Alumnos.objects.filter(carrera='TI').filter(turno='Matutino')
     #Consulta una sola condicion
     return render(request, "registro/consultas.html",{'8A':alumnos})

def consultar3(request):
     #Si solo deseamos recuperar ciertos datos agregamos la
     #funcion only, listando los campos que queremos obtener de
     #la consulta emplear filter() o #en el ejemplo all()
     alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
     #Consulta una sola condicion
     return render(request, "registro/consultas.html",{'8A':alumnos})

def consultar4(request):
     alumnos=Alumnos.objects.filter(turno__contains='Vesp')
     return render(request, "registro/consultas.html",{'8A':alumnos})

def consultar5(request):
     alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
     return render(request, "registro/consultas.html",{'8A':alumnos})

def consultar6(request):
     fechaInicio = datetime.date(2026, 2, 12)
     fechaFin = datetime.date(2026, 4, 10)
     alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
     return render(request, "registro/consultas.html",{'8A':alumnos})

def consultar7(request):
     alumnos=Alumnos.objects.filter(comentario__coment__contains='No Inscrito')
     return render(request, "registro/consultas.html",{'8A':alumnos})

def archivos(request):
     if request.method == 'POST':
          form = FormArchivos(request.POST, request.FILES)
          if form.is_valid():
               titulo = request.POST['titulo']
               descripcion = request.POST['descripcion']
               archivo = request.FILES['archivo']
               insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
               insert.save()
               return render(request,"registro/archivos.html")
          else:
               messages.error(request, "Error al procesar el formulario")
     else:
          return render(request,"registro/archivos.html",{'archivo':Archivos})
     
def consultarSQL(request):
     alumnos=Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registro_alumnos WHERE carrera="TI" ORDER BY turno DESC')

     return render(request,"registro/consultas.html",{'8A':alumnos})
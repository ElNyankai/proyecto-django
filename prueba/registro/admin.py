from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields= ('created','update')
    list_display= ('matricula', 'nombre', 'carrera', 'turno')
    search_fields= ('matricula', 'nombre', 'carrera', 'turno') #Filtro de busqueda
    date_hierarchy= 'created' #Filta de busqueda por fecha
    list_filter= ('carrera', 'turno') #Filtración especifica (solo  para que tengan el mismo nombre)

    def get_readonly_fields(self, request, obj=None):
        #si el usuario pertenece al grupo de permisos "Usuarios"
        if request.user.groups.filter(name="Usuarios").exists():
            #Bloquea los campos
            return ('matricula','carrera','turno')
        if request.user.groups.filter(name="EditarEliminar").exists():
            return ('matricula','turno')
        #Cualquier otro usuario que no pertenece al grupo "Usuario"
        else:
            return ('created','update') 

admin.site.register(Alumnos,AdministrarModelo )

class AdministrarComentario(admin.ModelAdmin):
    list_display= ('id','coment')
    search_fields=('id','create')
    date_hierarchy='create'
    readonly_fields=('create','id')

admin.site.register(Comentario,AdministrarComentario)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display=('id','mensaje')
    search_fields=('id','created')
    date_hierarchy= 'created'
    readonly_fields=('created','id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)



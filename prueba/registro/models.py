from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Alumnos(models.Model): #Define estructura de nuestra tabla
    matricula= models.CharField(max_length=12,verbose_name='Mat') #Texto corto
    nombre= models.TextField() #Texto largo
    carrera= models.TextField()
    turno= models.CharField(max_length=10)
    imagen= models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created= models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación') #Fecha y tiempo
    update= models.DateTimeField(auto_now_add=True,verbose_name='Fecha de actualización')

    class Meta:
        verbose_name= "Alumno"
        verbose_name_plural= "Alumnos"
        ordering= ["-created"]
        #el menos indica que se ordenara del más reciernte al más viejo.

    def __str__(self): #Debe ser con doble guión
        return self.nombre
    #Indica que se mostrára el nombre como valor de la tabla

class Comentario(models.Model):
    id= models.AutoField(primary_key=True,verbose_name="Clave")
    alumno= models.ForeignKey(Alumnos,
                              on_delete= models.CASCADE,verbose_name="Alumno")
    create=models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment= RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name= "Comentario"
        verbose_name_plural= "Comentarios"
        ordering= ["-create"]
        #el menos indica que se ordenara del más reciernte al más viejo.
    
    def __str__(self): #Debe ser con doble guión
        return self.coment
    #Indica que se mostrára el comentario como valor de la tabla

class ComentarioContacto(models.Model):
    id= models.AutoField(primary_key=True, verbose_name="Clave")
    usuario= models.TextField(verbose_name="Usuario")
    mensaje= models.TextField(verbose_name="Comentario")
    created= models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name="Comentario Contacto"
        verbose_name_plural= "Comentarios Contactos"
        ordering= ["-created"]

    def __str__(self):
        return self.mensaje
    #Indica que se mostrara el mensaje como valor en la tabla 

class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]

        def __str__(self):
            return self.titulo
from django.db import models

# Create your models here.
class producto (models.Model):

    id_producto = models.AutoField(primary_key = True, db_column = 'id_producto', verbose_name = 'ID_producto')
    nombre_producto = models.CharField(max_length = 20, blank = False, null = False)
    descripcion_producto = models.CharField(max_length = 150, blank = False, null = False)
    precio = models.IntegerField()
    stock = models.PositiveSmallIntegerField()
    metros = models.FloatField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return str(self.nombre_producto)
    
class carrito (models.Model):

    id_carrito = models.AutoField(primary_key = True, db_column = 'id_producto', verbose_name = 'ID_producto')
    id_usuario = models.ForeignKey('usuario', on_delete=models.CASCADE, db_column = 'id_usuario')

class producto_carrito (models.Model):

    id_producto = models.ForeignKey('producto', on_delete=models.CASCADE, db_column = 'id_producto')
    id_carrito = models.ForeignKey('carrito', on_delete=models.CASCADE, db_column = 'id_carrito')
    cantidad = models.PositiveSmallIntegerField()
    total = models.IntegerField()

class tipoUsuario (models.Model):

    id_tipo = models.AutoField(primary_key = True, db_column = 'id_tipo', verbose_name = 'ID_tipo_Usuario')
    tipo_usuario = models.CharField(max_length = 20, blank = False, null = False)

    def __str__(self):
        return str(self.tipo_usuario)
    
class usuario(models.Model):

    id_usuario = models.AutoField(primary_key = True, db_column='id_usuario', verbose_name='ID_usuario')
    rut_usuario = models.CharField(max_length = 10, blank = False, null = False)
    dv_usuario = models.CharField(max_length = 1, blank = False, null = False)
    nombre = models.CharField(max_length = 25, blank = False, null = False)
    appaterno = models.CharField(max_length = 25, blank = False, null = False)
    apmaterno = models.CharField(max_length = 25, blank = False, null = False)
    telefono = models.CharField(max_length = 10, blank = True, null = False)
    correo_usuario = models.CharField(max_length = 50, blank = False, null = False)
    contra_usuario = models.CharField(max_length = 50, blank = False, null = False)
    direccion_usuario = models.CharField(max_length = 50, blank = False, null = False)
    region_usuario = models.CharField(max_length = 100, blank = False, null = True)
    comuna_usuario = models.CharField(max_length = 100, blank = False, null = True)
    id_tipo = models.ForeignKey('tipoUsuario', on_delete = models.CASCADE, db_column = 'id_tipo')
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre) + " " + str(self.appaterno) + " " + str(self.apmaterno)
        
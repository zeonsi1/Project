from django.db import models

# Create your models here.
class producto (models.Model):

    id_producto = models.AutoField(primary_key = True, db_column = 'id_producto', verbose_name = 'ID_producto')
    nombre_producto = models.CharField(max_length = 20, blank = False, null = False)
    descripcion_producto = models.CharField(max_length = 150, blank = False, null = False)
    precio = models.IntegerField()
    stock = models.PositiveSmallIntegerField()
    metros = models.PositiveSmallIntegerField()

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
    
class region (models.Model):

    id_region = models.AutoField(primary_key = True, db_column = 'id_region', verbose_name = 'ID_region')
    region = models.CharField(max_length = 70, blank = False, null = False)

    def __str__(self):
        return str(self.region)

class comuna (models.Model):

    id_comuna = models.AutoField(primary_key = True, db_column = 'id_comuna', verbose_name = 'ID_comuna')
    comuna = models.CharField(max_length = 70, blank = False, null = False)
    id_region = models.ForeignKey('region', on_delete = models.CASCADE, db_column = 'id_region')

    def __str__(self):
        return str(self.comuna)
    
class usuario(models.Model):

    id_usuario = models.CharField(primary_key = True, max_length = 6)
    rut_usuario = models.CharField(max_length = 10, blank = False, null = False)
    dv_usuario = models.CharField(max_length = 1, blank = False, null = False)
    pnombre = models.CharField(max_length = 25, blank = False, null = False)
    snombre = models.CharField(max_length = 25, blank = True, null = True)
    appaterno = models.CharField(max_length = 25, blank = False, null = False)
    apmaterno = models.CharField(max_length = 25, blank = False, null = False)
    fecha_nacimiento = models.DateField(blank = False, null = False)
    correo_usuario = models.CharField(max_length = 50, blank = False, null = False)
    contra_usuario = models.CharField(max_length = 50, blank = False, null = False)
    direccion_usuario = models.CharField(max_length = 50, blank = False, null = False)
    id_comuna = models.ForeignKey('comuna', on_delete = models.CASCADE, db_column = 'id_comuna')
    id_tipo = models.ForeignKey('tipoUsuario', on_delete = models.CASCADE, db_column = 'id_tipo')
    activo = models.IntegerField()

    def __str__(self):

        if str(self.snombre) != "":
            return str(self.pnombre) + " " + str(self.snombre) + " " + str(self.appaterno) + " " + str(self.apmaterno)
        else:
            return str(self.pnombre) + " " + str(self.appaterno) + " " + str(self.apmaterno)
        
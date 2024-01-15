from django.db import models

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

class Registros(models.Model):
    id = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    precio = models.IntegerField()
    id_divisa = models.IntegerField()  

class Divisas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.IntegerField()  
    simbolo = models.IntegerField()  

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.IntegerField()  

class ProductosCategorizados(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('producto', 'categoria')  # Esto es equivalente a PRIMARY KEY (Producto,Categoria) en SQL

class Monedas(models.Model):
    id = models.AutoField(primary_key=True)
    id_divisa = models.ForeignKey(Divisas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    valor = models.IntegerField()

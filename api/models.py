from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=255)

class Registros(models.Model):
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=255)
    precio = models.IntegerField()
    id_divisa = models.ForeignKey('Divisas', on_delete=models.CASCADE)

class Divisas(models.Model):
    nombre = models.CharField(max_length=255)
    simbolo = models.CharField(max_length=10)

class Categorias(models.Model):
    nombre = models.CharField(max_length=255)

class ProductosCategorizados(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

class Monedas(models.Model):
    id_divisa = models.ForeignKey(Divisas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    valor = models.IntegerField()

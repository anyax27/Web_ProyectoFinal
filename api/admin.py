from django.contrib import admin
from .models import Productos, Registros, Divisas, Categorias, ProductosCategorizados, Monedas

# Register your models here.
admin.site.register(Productos)
admin.site.register(Registros)
admin.site.register(Divisas)
admin.site.register(Categorias)
admin.site.register(ProductosCategorizados)
admin.site.register(Monedas)

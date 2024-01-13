from rest_framework import viewsets
from .serializer import ProductosSerializer, RegistrosSerializer, DivisasSerializer, CategoriasSerializer, ProductosCategorizadosSerializer, MonedasSerializer
from .models import Productos, Registros, Divisas, Categorias, ProductosCategorizados, Monedas

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    
class RegistrosViewSet(viewsets.ModelViewSet):
    queryset = Registros.objects.all()
    serializer_class = RegistrosSerializer

class DivisasViewSet(viewsets.ModelViewSet):
    queryset = Divisas.objects.all()
    serializer_class = DivisasSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class ProductosCategorizadosViewSet(viewsets.ModelViewSet):
    queryset = ProductosCategorizados.objects.all()
    serializer_class = ProductosCategorizadosSerializer

class MonedasViewSet(viewsets.ModelViewSet):
    queryset = Monedas.objects.all()
    serializer_class = MonedasSerializer

from rest_framework import serializers
from .models import Productos, Registros, Divisas, Categorias, ProductosCategorizados, Monedas

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
        
class RegistrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registros
        fields = '__all__'
        
class DivisasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisas
        fields = '__all__'
        
class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
        
class ProductosCategorizadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosCategorizados
        fields = '__all__'
        
class MonedasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monedas
        fields = '__all__'
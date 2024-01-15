from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.parsers import JSONParser
from .models import Productos, Registros, Divisas, Categorias, ProductosCategorizados, Monedas
from .serializers import ProductosSerializer, RegistrosSerializer, DivisasSerializer, CategoriasSerializer, ProductosCategorizadosSerializer, MonedasSerializer

# Vistas para el modelo Productos
@method_decorator(csrf_exempt, name='dispatch')
class ProductosApi(View):
    def get(self, request, id=0):
        if id == 0:
            productos = Productos.objects.all()
            serializer = ProductosSerializer(productos, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            producto = Productos.objects.get(id=id)
            serializer = ProductosSerializer(producto)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        producto_data = JSONParser().parse(request)
        serializer = ProductosSerializer(data=producto_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    def put(self, request, id = None):
        producto_data = JSONParser().parse(request)
        producto = Productos.objects.get(id=id)
        serializer = ProductosSerializer(producto, data=producto_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    def delete(self, request, id):
        producto = Productos.objects.get(id=id)
        producto.delete()
        return JsonResponse("Deleted Successfully", safe=False)


# Vistas para el modelo Registros
@method_decorator(csrf_exempt, name='dispatch')
class RegistrosApi(View):
    def get(self, request, id=0):
        if id == 0:
            registros = Registros.objects.all()
            serializer = RegistrosSerializer(registros, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            registro = Registros.objects.get(id=id)
            serializer = RegistrosSerializer(registro)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        registro_data = JSONParser().parse(request)
        serializer = RegistrosSerializer(data=registro_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    def put(self, request, id):
        registro_data = JSONParser().parse(request)
        registro = Registros.objects.get(id=id)
        serializer = RegistrosSerializer(registro, data=registro_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    def delete(self, request, id):
        registro = Registros.objects.get(id=id)
        registro.delete()
        return JsonResponse("Deleted Successfully", safe=False)


# Vistas para el modelo Divisas
@method_decorator(csrf_exempt, name='dispatch')
class DivisasApi(View):
    def get(self, request, id=0):
        if id == 0:
            divisas = Divisas.objects.all()
            serializer = DivisasSerializer(divisas, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            divisa = Divisas.objects.get(id=id)
            serializer = DivisasSerializer(divisa)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        divisa_data = JSONParser().parse(request)
        serializer = DivisasSerializer(data=divisa_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    def put(self, request, id):
        divisa_data = JSONParser().parse(request)
        divisa = Divisas.objects.get(id=id)
        serializer = DivisasSerializer(divisa, data=divisa_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    def delete(self, request, id):
        divisa = Divisas.objects.get(id=id)
        divisa.delete()
        return JsonResponse("Deleted Successfully", safe=False)


# Vistas para el modelo Categorias
@method_decorator(csrf_exempt, name='dispatch')
class CategoriasApi(View):
    def get(self, request, id=0):
        if id == 0:
            categorias = Categorias.objects.all()
            serializer = CategoriasSerializer(categorias, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            categoria = Categorias.objects.get(id=id)
            serializer = CategoriasSerializer(categoria)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        categoria_data = JSONParser().parse(request)
        serializer = CategoriasSerializer(data=categoria_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    def put(self, request, id):
        categoria_data = JSONParser().parse(request)
        categoria = Categorias.objects.get(id=id)
        serializer = CategoriasSerializer(categoria, data=categoria_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    def delete(self, request, id):
        categoria = Categorias.objects.get(id=id)
        categoria.delete()
        return JsonResponse("Deleted Successfully", safe=False)


# Vistas para el modelo ProductosCategorizados
@method_decorator(csrf_exempt, name='dispatch')
class ProductosCategorizadosApi(View):
    def get(self, request, id=0):
        if id == 0:
            productos_categorizados = ProductosCategorizados.objects.all()
            serializer = ProductosCategorizadosSerializer(productos_categorizados, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            producto_categorizado = ProductosCategorizados.objects.get(id=id)
            serializer = ProductosCategorizadosSerializer(producto_categorizado)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        producto_categorizado_data = JSONParser().parse(request)
        serializer = ProductosCategorizadosSerializer(data=producto_categorizado_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    def put(self, request, id):
        producto_categorizado_data = JSONParser().parse(request)
        producto_categorizado = ProductosCategorizados.objects.get(id=id)
        serializer = ProductosCategorizadosSerializer(producto_categorizado, data=producto_categorizado_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    def delete(self, request, id):
        producto_categorizado = ProductosCategorizados.objects.get(id=id)
        producto_categorizado.delete()
        return JsonResponse("Deleted Successfully", safe=False)


# Vistas para el modelo Monedas
@method_decorator(csrf_exempt, name='dispatch')
class MonedasApi(View):
    def get(self, request, id=0):
        if id == 0:
            monedas = Monedas.objects.all()
            serializer = MonedasSerializer(monedas, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            moneda = Monedas.objects.get(id=id)
            serializer = MonedasSerializer(moneda)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        moneda_data = JSONParser().parse(request)
        serializer = MonedasSerializer(data=moneda_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    def put(self, request, id):
        moneda_data = JSONParser().parse(request)
        moneda = Monedas.objects.get(id=id)
        serializer = MonedasSerializer(moneda, data=moneda_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    def delete(self, request, id):
        moneda = Monedas.objects.get(id=id)
        moneda.delete()
        return JsonResponse("Deleted Successfully", safe=False)

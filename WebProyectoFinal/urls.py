from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from AppWeb import views

urlpatterns = [
    # URLs para el modelo Productos
    path('productos/', views.ProductosApi.as_view(), name='productos-list'),
    path('productos/<int:id>/', views.ProductosApi.as_view(), name='productos-detail'),

    # URLs para el modelo Registros
    path('registros/', views.RegistrosApi.as_view(), name='registros-list'),
    path('registros/<int:id>/', views.RegistrosApi.as_view(), name='registros-detail'),

    # URLs para el modelo Divisas
    path('divisas/', views.DivisasApi.as_view(), name='divisas-list'),
    path('divisas/<int:id>/', views.DivisasApi.as_view(), name='divisas-detail'),

    # URLs para el modelo Categorias
    path('categorias/', views.CategoriasApi.as_view(), name='categorias-list'),
    path('categorias/<int:id>/', views.CategoriasApi.as_view(), name='categorias-detail'),

    # URLs para el modelo ProductosCategorizados
    path('productos-categorizados/', views.ProductosCategorizadosApi.as_view(), name='productos-categorizados-list'),
    path('productos-categorizados/<int:id>/', views.ProductosCategorizadosApi.as_view(), name='productos-categorizados-detail'),

    # URLs para el modelo Monedas
    path('monedas/', views.MonedasApi.as_view(), name='monedas-list'),
    path('monedas/<int:id>/', views.MonedasApi.as_view(), name='monedas-detail'),

    # URL del admin
    path('admin/', admin.site.urls),

]

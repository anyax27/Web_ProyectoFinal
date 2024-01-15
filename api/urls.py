from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'PRODUCTO', views.ProductosViewSet)
router.register(r'REGISTRO', views.RegistrosViewSet)
router.register(r'DIVISA', views.DivisasViewSet)
router.register(r'CATEGORIA', views.CategoriasViewSet)
router.register(r'PRODUCTO_CATEGORIZADO', views.ProductosCategorizadosViewSet)
router.register(r'MONEDA', views.MonedasViewSet)

urlpatterns = [
    path('', include(router.urls))
]

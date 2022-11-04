from django.urls import path,include
from healthyapp import views

urlpatterns = [
    path('',views.Producto_lista),
    path('api/healthyapp',views.Producto_lista),
    path('api/healthyapp/<int:pk>',views.Producto_detalle),
    path('api/categorias',views.Categoria_lista),
    path('api/categorias/<int:pk>',views.Categoria_detalle)
    #  path('api/users/<int:pk>',views.user)
]

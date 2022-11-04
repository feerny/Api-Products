from rest_framework import serializers
from healthyapp.models import Producto
from .models import Categoria


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields ='__all__'
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields ='__all__'
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Producto
#         fields =(
#             "id",
#             "nombre",
#             "email",
#             "contraseña"
#         )
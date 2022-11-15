from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from healthyapp.models import Producto
from healthyapp.models import Categoria
from healthyapp.serializers import ProductosSerializer  
from healthyapp.serializers import CategoriaSerializer 
from rest_framework.decorators import api_view


@api_view(['GET','POST','DELETE'])
def Producto_lista(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        
        
        titulo=request.GET.get('titulo',None)
        if titulo is not None:
            productos = productos.filter(titulo__icontains=titulo)
        productos_serializer=ProductosSerializer(productos,many=True)
        return JsonResponse(productos_serializer.data, safe=False)
    
    elif request.method == 'POST':
        producto_data=JSONParser().parse(request)
        producto_serializer=ProductosSerializer(data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return JsonResponse(producto_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Producto.objects.all().delete()
        return JsonResponse({'message':'{} el producto eliminado satisfactoriamente!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)
   
@api_view(['GET','PUT','DELETE']) 
def Producto_detalle(request,pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return JsonResponse({'message':'producto no existe!'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        producto_serializer=ProductosSerializer(producto)
        return JsonResponse(producto_serializer.data)
    
    elif request.method=='PUT':
        producto_data=JSONParser().parse(request)
        producto_serializer=ProductosSerializer(producto,data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return JsonResponse(producto_serializer.data)
    
    elif request.method=='DELETE':
        producto.delete()
        return JSONParser({'message':'producto a sido borrado!'},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST','DELETE'])
def Categoria_lista(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        
        
        titulo=request.GET.get('titulo',None)
        if titulo is not None:
            categoria = categoria.filter(titulo__icontains=titulo)
        categoriaSerializer=CategoriaSerializer(categoria,many=True)
        return JsonResponse(categoriaSerializer.data, safe=False)
    
    elif request.method == 'POST':
        categoria_data=JSONParser().parse(request)
        categoriaSerializer=CategoriaSerializer(data=categoria_data)
        if categoriaSerializer.is_valid():
            categoriaSerializer.save()
            return JsonResponse(categoriaSerializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(categoriaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Categoria.objects.all().delete()
        return JsonResponse({'message':'{} categoria eliminada satisfactoriamente!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)
   
@api_view(['GET','PUT','DELETE']) 
def Categoria_detalle(request,pk):
    
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return JsonResponse({'message':'categoria no existe!'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        categoriaSerializer=CategoriaSerializer(categoria)
        return JsonResponse(categoriaSerializer.data)
    
    elif request.method=='PUT':
        categoria_data=JSONParser().parse(request)
        categoriaSerializer=CategoriaSerializer(categoria,data=categoria_data)
        if categoriaSerializer.is_valid():
            categoriaSerializer.save()
            return JsonResponse(categoriaSerializer.data)
    
    elif request.method=='DELETE':
        categoria.delete()
        return JSONParser({'message':'categoria a sido borrada!'},status=status.HTTP_204_NO_CONTENT)
    
    

    
    

        

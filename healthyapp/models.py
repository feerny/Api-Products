from tokenize import blank_re
from django.db import models


class Categoria(models.Model):
    nombre= models.CharField(max_length=100,blank=False,default='')
    
    def __str__(self):
          
        return self.nombre
class Producto(models.Model):
    nombre= models.CharField(max_length=100,blank=False,default='')
    price = models.FloatField()
    cantidad = models.IntegerField(default=300)
    descripcion= models.TextField()
    imagen = models.ImageField(upload_to='images', null=True )
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
          
        return self.nombre
    

    
    
# class User(models.Model):
#     nombre= models.CharField(max_length=100,blank=False,default='')
#     email = models.IntegerField()
#     contrasña= models.TextField()
    
#     def __str__(self):
#         return self.nombre

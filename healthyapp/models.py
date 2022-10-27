from tokenize import blank_re
from django.db import models

class Producto(models.Model):
    nombre= models.CharField(max_length=100,blank=False,default='')
    price = models.IntegerField()
    descripcion= models.TextField()
    imagen = models.ImageField(upload_to='images', null=True )
    
    def __str__(self):
          
        return self.nombre
    
    
# class User(models.Model):
#     nombre= models.CharField(max_length=100,blank=False,default='')
#     email = models.IntegerField()
#     contrasña= models.TextField()
    
#     def __str__(self):
#         return self.nombre

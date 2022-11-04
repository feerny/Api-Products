from django.contrib import admin
from .models import Producto
from .models import Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display= ["nombre","price","descripcion"]
    list_editable= ["price"]
    search_fields = ["nombre"]
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display= ["nombre"]
    search_fields = ["nombre"]

    
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria,CategoriaAdmin)

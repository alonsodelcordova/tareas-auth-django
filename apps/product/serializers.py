from tareas_django.utils.base_serializers import DynamicFieldsModelSerializer

from .models import Categoria, Producto

class CategorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id', 
            'nombre', 
            'descripcion'
        ]
        
class ProductSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'id', 
            'nombre', 
            'precio', 
            'descripcion', 
            'imagen', 
            'stock', 
            'categoria'
        ]
        extra_kwargs = {
            'imagen': {'read_only': True},
            'stock': {'read_only': True}
        }
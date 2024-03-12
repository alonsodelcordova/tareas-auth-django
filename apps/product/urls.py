from django.urls import re_path, path
from .api import  CategoriaApiView, ProductoApiView, ProductoUpdateView

urlpatterns = [
    path('producto/imagen/<int:id>', ProductoUpdateView.as_view() ),
    path('categoria', CategoriaApiView.as_view() ),
    path('producto', ProductoApiView.as_view() ),
    
]
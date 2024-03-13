from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import status, views, viewsets
from .models import Categoria, Producto

    
    
class CategoriaApiView(views.APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategorySerializer(categorias, many=True)
        return Response(serializer.data)

class ProductoApiView(views.APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data)
    
class ProductoUpdateView(views.APIView):
    
    def get(self, request, id):
        try:
            producto = Producto.objects.get(id=id)
            serializer = ProductSerializer(producto)
            return Response(serializer.data)
        except Producto.DoesNotExist:
            return Response({'msg':'Producto no encontrado.'},status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        try:
            if 'imagen' not in request.data:
                return Response({'msg':'Imagen no encontrada.'},status=status.HTTP_400_BAD_REQUEST)
            producto = Producto.objects.get(id=id)
            producto.imagen = request.data['imagen']
            producto.save()
            return Response({'msg':'Imagen actualizada correctamente.'},status=status.HTTP_200_OK)
        except Producto.DoesNotExist:
            return Response({'msg':'Producto no encontrado.'},status=status.HTTP_404_NOT_FOUND)
        
# ingresar producto

@api_view(['POST'])
def ingresarProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        cantidad = request.data['cantidad']
        producto.stock += cantidad
        producto.save()
        return Response({'msg':'Producto ingresado correctamente.'},status=status.HTTP_200_OK)
    except Producto.DoesNotExist:
        return Response({'msg':'Producto no encontrado.'},status=status.HTTP_404_NOT_FOUND)


# venta de producto
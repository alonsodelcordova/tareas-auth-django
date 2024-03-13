from django.db import models
from apps.product.models import Producto
# Create your models here.

class Venta(models.Model):
    cliente = models.CharField(max_length=100)
    tipo_comprobante = models.CharField(max_length=20)
    serie_comprobante = models.CharField(max_length=25)
    numero_comprobante = models.CharField(max_length=25)
    fecha = models.DateField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class VentaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.producto.nombre
    
    class Meta:
        verbose_name = 'VentaProducto'
        verbose_name_plural = 'Ventas Productos'
        ordering = ['id']
    
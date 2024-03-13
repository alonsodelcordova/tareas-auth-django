from django.db import models
from apps.product.models import Producto
# Create your models here.

class Ingreso(models.Model):
    proveedor = models.CharField(max_length=100)
    tipo_comprobante = models.CharField(max_length=20)
    serie_comprobante = models.CharField(max_length=25)
    numero_comprobante = models.CharField(max_length=25)
    fecha = models.DateField(auto_now_add=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        ordering = ['id']
    


class IngresoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.producto.nombre + ' - S/. ' + self.precio_unitario
    
    class Meta:
        verbose_name = 'IngresoProducto'
        verbose_name_plural = 'Ingresos Productos'
        ordering = ['id']
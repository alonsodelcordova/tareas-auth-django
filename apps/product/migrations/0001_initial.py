# Generated by Django 5.0.3 on 2024-03-12 03:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('stock', models.IntegerField(blank=True, default=0, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producto')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producto')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id'],
            },
        ),
    ]

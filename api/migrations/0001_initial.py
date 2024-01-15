# Generated by Django 5.0 on 2023-12-10 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_cat", models.CharField(max_length=100)),
                ("material_hecho", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombreProducto", models.CharField(max_length=100)),
                ("precio", models.IntegerField()),
                ("img_produc", models.ImageField(upload_to="imagenes/")),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.categoria"
                    ),
                ),
            ],
        ),
    ]

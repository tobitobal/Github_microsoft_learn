# Generated by Django 5.0.1 on 2024-01-11 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_modelo_remove_producto_version_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Modelo',
            new_name='Version',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='modelos',
            new_name='version',
        ),
    ]

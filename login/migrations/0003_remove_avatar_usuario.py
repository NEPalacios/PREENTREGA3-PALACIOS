# Generated by Django 5.0.6 on 2024-06-15 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_name_avatar_nombre_de_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='usuario',
        ),
    ]

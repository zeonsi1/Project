# Generated by Django 4.2.1 on 2023-07-07 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impekbles', '0007_remove_usuario_id_comuna_usuario_comuna_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='pnombre',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nacimiento',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='snombre',
        ),
    ]
# Generated by Django 4.2.1 on 2023-07-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impekbles', '0008_rename_pnombre_usuario_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id_usuario',
            field=models.AutoField(db_column='id_usuario', primary_key=True, serialize=False, verbose_name='ID_usuario'),
        ),
    ]
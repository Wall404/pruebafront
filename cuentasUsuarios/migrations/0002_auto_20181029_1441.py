# Generated by Django 2.1.2 on 2018-10-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentasUsuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_academica',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_academica_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_departamento',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_dir_prog_curricular',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_director_carrera',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_docente',
            field=models.BooleanField(default=False),
        ),
    ]
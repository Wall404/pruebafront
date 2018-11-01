# Generated by Django 2.1.2 on 2018-11-01 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentasUsuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuarioAcademica',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('changedOn', models.DateTimeField(null=True)),
            ],
        ),
    ]

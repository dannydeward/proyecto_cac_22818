# Generated by Django 3.2.14 on 2022-12-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servinquilino', '0003_alter_login_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensa',
            name='dni',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='DNI'),
        ),
    ]

# Generated by Django 2.2.4 on 2019-11-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piezas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieza',
            name='observaciones',
            field=models.CharField(max_length=400),
        ),
    ]
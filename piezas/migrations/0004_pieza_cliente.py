# Generated by Django 2.2.4 on 2019-11-12 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20191112_1151'),
        ('piezas', '0003_auto_20191112_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='pieza',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
            preserve_default=False,
        ),
    ]

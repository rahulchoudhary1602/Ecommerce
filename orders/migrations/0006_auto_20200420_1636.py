# Generated by Django 2.2 on 2020-04-20 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200419_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
        ),
    ]

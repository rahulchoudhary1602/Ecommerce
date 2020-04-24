# Generated by Django 2.2 on 2020-04-19 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_auto_20200418_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='final_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='tax_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orders',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
        ),
    ]

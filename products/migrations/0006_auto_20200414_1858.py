# Generated by Django 2.2 on 2020-04-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200412_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='placeholder-300x169.jpg', upload_to='static/media'),
        ),
    ]

# Generated by Django 4.2 on 2023-12-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_factory_lat_coord_factory_long_coord'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='image',
            field=models.ImageField(null=True, upload_to='factory_images/%Y/%m', verbose_name='Картинка завода'),
        ),
    ]

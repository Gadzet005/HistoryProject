# Generated by Django 4.2 on 2023-12-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='lat_coord',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='factory',
            name='long_coord',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=8),
        ),
    ]

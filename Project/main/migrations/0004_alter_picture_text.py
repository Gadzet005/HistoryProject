# Generated by Django 4.2 on 2023-12-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_factory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='text',
            field=models.CharField(max_length=100, null=True, verbose_name='Подпись'),
        ),
    ]

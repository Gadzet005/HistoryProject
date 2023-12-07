# Generated by Django 4.2 on 2023-12-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_picture_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='is_factory',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Подпись'),
        ),
    ]
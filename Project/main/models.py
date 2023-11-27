from django.db import models


class Exhibit(models.Model):
    title = models.CharField(verbose_name="Имя", max_length=100)
    content = models.TextField(verbose_name="Статья")

    class Meta:
        abstract = True


class Factory(Exhibit):
    pass

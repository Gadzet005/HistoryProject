from django.db import models
from django.urls import reverse


class Exhibit(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание")

    class Meta:
        abstract = True


class Factory(Exhibit):
    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"
    
    def get_absolute_url(self):
        return reverse('main:factory', kwargs={'factory_id': self.pk})


class Picture(models.Model):
    image = models.ImageField("Картинка", upload_to="images/%Y/%m")
    text = models.CharField("Подпись", max_length=100)
    factory = models.ForeignKey(
        Factory, verbose_name="Фабрика", on_delete=models.CASCADE
    )

    class Meta:
        default_related_name = "pictures"

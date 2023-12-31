from django.db import models
from django.urls import reverse


class Factory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание")
    lat_coord = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)
    long_coord = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)
    image = models.ImageField("Картинка завода", upload_to="factory_images/%Y/%m", null=True)
    is_factory = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def get_absolute_url(self):
        return reverse('main:factory', kwargs={'factory_id': self.pk})


class Picture(models.Model):
    image = models.ImageField("Картинка", upload_to="images/%Y/%m")
    text = models.CharField("Подпись", max_length=100, null=True, blank=True)
    factory = models.ForeignKey(
        Factory, verbose_name="Фабрика", on_delete=models.CASCADE,
    )

    class Meta:
        default_related_name = "pictures"


class Article(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = models.TextField(verbose_name="Текст")
    next = models.ForeignKey(
        "self", verbose_name="Следующая статья", on_delete=models.SET_NULL,
        null=True, blank=True
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:article', kwargs={'article_id': self.pk})

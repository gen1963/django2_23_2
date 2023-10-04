from django.db import models


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='uploads', verbose_name="Фото")
    description = models.CharField(max_length=50, verbose_name="Опис")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
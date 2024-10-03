from django.db import models
from .utils import image_order_next_val


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def save(self, *args, **kwargs):
        if self.order is None:
            self.order = image_order_next_val()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

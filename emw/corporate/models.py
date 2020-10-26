from django.db import models

# Create your models here.


class Slider(models.Model):
    background_image = models.ImageField(
        upload_to='bg/')
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    button_title = models.CharField(max_length=255)
    button_link = models.URLField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    position = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["position", ]

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class FAQs(models.Model):
    question = models.CharField(max_length=255, unique=True)
    answer = RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'Frequently Asked Questions'

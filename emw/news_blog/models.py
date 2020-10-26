from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class BlogNews(models.Model):
    OPTION = (
        ('', 'Select Category'),
        ('news', 'News'),
        ('articles', 'Articles'),

    )
    category = models.CharField(max_length=50, choices=OPTION)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Admin')
    image = models.ImageField(upload_to='blog/%Y/%m/')
    description = RichTextUploadingField()
    tag = models.ManyToManyField('Tag')
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'News or Article'

    # def get_absolute_url(self):
    #     return reverse('blog:articles-details',kwargs={'slug':self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']

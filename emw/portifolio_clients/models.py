from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(
        upload_to='logo/')
    updated = models.DateTimeField(auto_now=True)
    position = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["position", ]


class Project(models.Model):
    CATEGORY = (
        ('', 'Choose Category'),
        ('contracting', 'contracting'),
        ('logistics', 'Logistics')
    )
    company = models.CharField(max_length=255)
    project_category = models.CharField(max_length=100, choices=CATEGORY)
    project_name = models.CharField(max_length=255)
    project_description = RichTextUploadingField()
    project_cover_image = models.ImageField(
        upload_to='project/%Y/%m/')
    slug = models.SlugField(unique=True)
    updated = models.DateTimeField(auto_now=True)
    position = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company + ' ' + self.project_name

    class Meta:
        ordering = ["position", ]


class Gallery(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    small_text = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='project/%Y/%m/')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.project_name + ' '+self.small_text

    class Meta:
        ordering = ["timestamp", ]
        verbose_name_plural = 'Gallery'

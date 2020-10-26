# Generated by Django 3.1.1 on 2020-09-30 08:51

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='BlogNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('', 'Select Category'), ('news', 'News'), ('article', 'Article')], max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(default='Admin', max_length=255)),
                ('image', models.ImageField(upload_to='blog/%Y/%m/')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ManyToManyField(related_name='blog', to='news_blog.Tag')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-30 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blognews',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'News or Article'},
        ),
    ]

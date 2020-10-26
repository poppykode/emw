from django.contrib import admin
from .models import BlogNews, Tag

# Register your models here.


class BlogNewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = BlogNews


admin.site.register(BlogNews, BlogNewsAdmin)
admin.site.register(Tag)

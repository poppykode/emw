from django.contrib import admin
from .models import (
    Client,
    Project,
    Gallery
)

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("project_name", "company")}

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)
admin.site.register(Client)
admin.site.register(Gallery)

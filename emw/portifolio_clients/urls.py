from django.urls import path
from .views import (
    project_details,
    projects
)


app_name = 'portifolio_clients'
urlpatterns = [
    path('project/<slug:slug>', project_details, name='project_details'),
    path('projects/all', projects, name='projects')

]

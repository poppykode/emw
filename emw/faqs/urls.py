from django.urls import path
from .views import faqs


app_name = 'faqs'
urlpatterns = [
    path('help/faqs', faqs, name="faqs"),

]

from django.urls import path
from .views import (
    home,
    contact,
    contracting,
    logistics,
    construction_and_civils,
    joinery,
    steel_fabrication,
    general_trucks,
    specialised_trucks,
)

app_name = 'corporate'
urlpatterns = [
    path('', home, name='home'),
    path('contact-us', contact, name='contact'),
    path('contracting', contracting, name='contracting'),
    path('logistics', logistics, name='logistics'),
    path('contracting/construction-and-civils',
         construction_and_civils, name='construction_and_civils'),
    path('contracting/joinery', joinery, name='joinery'),
    path('contracting/steel-fabrication',
         steel_fabrication, name='steel_fabrication'),
    path('logistics/general-trucks', general_trucks, name='general_trucks'),
    path('logistics/specialised-trucks',
         specialised_trucks, name='specialised_trucks'),

]

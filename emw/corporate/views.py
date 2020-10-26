from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import (
    Slider
)
from portifolio_clients.models import (
    Client, Project
)
from news_blog.models import BlogNews
from .utils import send_email

# Create your views here.


def home(request):
    template_name = 'corporate/home.html'
    sliders_qs = Slider.objects.all()
    blog_news_qs = BlogNews.objects.all()[:1]
    project_qs = Project.objects.all()[:3]
    context = {
        'sliders': sliders_qs,
        'blog_news': blog_news_qs,
        'projects': project_qs
    }
    return render(request, template_name, context)


def contact(request):
    template_name = 'corporate/contact.html'
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')
        send_email(request, name, email, subject, textarea)
    return render(request, template_name)


def logistics(request):
    template_name = 'corporate/services/logistics_overview.html'
    return render(request, template_name)


def contracting(request):
    template_name = 'corporate/services/contracting_overview.html'
    return render(request, template_name)

# contracting services


def construction_and_civils(request):
    template_name = 'corporate/services/contracting_civil.html'
    return render(request, template_name)


def joinery(request):
    template_name = 'corporate/services/contracting_joinery.html'
    return render(request, template_name)


def steel_fabrication(request):
    template_name = 'corporate/services/contracting_steel_fabrication.html'
    return render(request, template_name)

# logistics servies


def general_trucks(request):
    template_name = 'corporate/services/logistics_general_trucks.html'
    return render(request, template_name)


def specialised_trucks(request):
    template_name = 'corporate/services/logistics_specialised_trucks.html'
    return render(request, template_name)

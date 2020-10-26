from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import (
    Project
)

# Create your views here.


def project_details(request, slug):
    template_name = 'portifolio_clients/project_details.html'
    qs = get_object_or_404(Project, slug=slug)
    return render(request, template_name, {'obj': qs})


def projects(request):
    template_name = 'portifolio_clients/projects.html'
    qs_projs = Project.objects.all()
    paginator = Paginator(qs_projs, 36)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    return render(request, template_name, {'obj': qs, })

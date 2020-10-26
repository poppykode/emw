from django.shortcuts import render
from .models import FAQs

# Create your views here.


def faqs(request):
    template_name = 'faqs/faqs.html'
    qs = FAQs.objects.all()
    return render(request, template_name, {'obj': qs})

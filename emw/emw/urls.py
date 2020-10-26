"""emw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# default: "Django Administration"
admin.site.site_header = 'EMW Admin'
# default: "Site administration"
# admin.site.index_title = 'Features area'
# default: "Django site admin"
# admin.site.site_title = 'HTML title from adminsitration'

urlpatterns = [
    path('emw/admin/', admin.site.urls),
    path('', include('corporate.urls')),
    path('faqs/', include('faqs.urls')),
    path('', include('news_blog.urls')),
    path('', include('portifolio_clients.urls')),
    path('queries/', include('queries.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

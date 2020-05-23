# -*- Mode: Python; coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
	path('orcamento/<int:id>/', views.orcamento, name='orcamento'),
    path('admin/', admin.site.urls),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
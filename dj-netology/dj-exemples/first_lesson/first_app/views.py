from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.urls import reverse


def home_url_view(request):
    info_url = reverse('info')
    return HttpResponse(f'Привет Мир! Для инфориации перейти <a href="{info_url}">Нажать</a>')


def home_view(request):
    return HttpResponse('Привет Мир!!!')


def info_view(request):
    dt = datetime.now()
    return HttpResponse(f'Info Page - {dt}')

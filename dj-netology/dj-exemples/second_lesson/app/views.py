from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def admin_email_view(request):
    data = settings.ADMIN_EMAIL
    return HttpResponse(f'Email - {data}')

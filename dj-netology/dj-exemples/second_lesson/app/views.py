from django.http import HttpResponse
from django.conf import settings
from datetime import datetime


def admin_email_view(request):
    data = settings.ADMIN_EMAIL
    return HttpResponse(f'Email - {data}')


def info_employee_view(request):
    data = {
        'Ivan': 'Начальник отдела',
        'Alex': 'Разработчик'
    }

    name = request.GET.get('name', 'не задан')
    info = data.get(name, 'Данные не найдены')

    return HttpResponse(f'Пользователь {name} - {info}')


def info_datetime_view(request, year, month, day):
    data = datetime(year, month, day)
    return HttpResponse(f'Дата/время - {data}')


def info_datetime_dtc_view(request, value):
    return HttpResponse(f'Дата/время - {value}')

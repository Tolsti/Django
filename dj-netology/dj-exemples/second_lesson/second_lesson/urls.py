from django.contrib import admin
from django.urls import path, register_converter
from app import views
from app.converter import DateConverter

register_converter(DateConverter, 'dtc')

urlpatterns = [
    path('', views.admin_email_view),
    path('admin/', admin.site.urls),
    path('admin_email/', views.admin_email_view),
    path('info/', views.info_employee_view),
    path('since/<int:year>-<int:month>-<int:day>/', views.info_datetime_view),
    path('since_dtc/<dtc:value>/',views.info_datetime_dtc_view)
]

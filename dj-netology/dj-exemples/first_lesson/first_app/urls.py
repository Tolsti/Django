from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.home_view),
    path('info_url/', views.home_url_view, name='url_info'),
    path('home/', views.home_view, name='home'),
    path('info/', views.info_view, name='info')
]

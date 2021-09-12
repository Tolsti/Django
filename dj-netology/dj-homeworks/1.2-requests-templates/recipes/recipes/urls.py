from django.urls import path
from calculator import views

urlpatterns = [
    path('<name>/', views.recipes_view)
]

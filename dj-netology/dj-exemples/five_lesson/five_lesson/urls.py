from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from app.api_view import car_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cars/', csrf_exempt(car_view)),
    # path('api-auth/', include('rest_framework.urls'))
]

import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from django.http import HttpResponse, JsonResponse
from .serializers import CarSerializer
from .models import Car


@api_view(http_method_names=['GET', 'POST'])
def car_view(request):
    # if request.method not in ['GET', 'POST']:
    #     return HttpResponse(status=405)

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        # data = [{'id': car.id, 'name': car.name} for car in cars]

        return Response(serializer.data, status=HTTP_200_OK)

    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        # проверка на валидные данные, drf сам обработает исключения
        serializer.is_valid(raise_exception=True)
        car = Car.objects.create(**serializer.validated_data)
        context = CarSerializer(car)

        # data = json.loads(request.body)
        # car = Car.objects.create(**data)
        # context = {'id': car.id, 'name': car.name}

        return Response(context.data, status=HTTP_201_CREATED)

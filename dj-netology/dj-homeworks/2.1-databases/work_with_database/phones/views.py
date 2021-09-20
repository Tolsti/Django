from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    phones = Phone.objects.all()

    if sort == 'name':
        phones = phones.order_by('name')
    if sort == 'max_price':
        phones = phones.order_by('-price')
    if sort == 'min_price':
        phones = phones.order_by('price')

    template = 'catalog.html'
    context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)

    template = 'product.html'
    context = {'phone': phone}

    return render(request, template, context)

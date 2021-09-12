from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
    # можете добавить свои рецепты ;)
}


def recipes_view(request, name):
    count = request.GET.get('servings')
    context = {'recipe': DATA[name]}

    if count is not None:
        context = {'recipe': {k: v * float(count) for k, v in DATA[name].items()}}

    return render(request, 'calculator/index.html', context)

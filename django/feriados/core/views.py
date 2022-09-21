from django.shortcuts import render


def natal(request):
    contexto = {'natal': True, 'carnaval': False}
    # import ipdb ; ipdb.set_trace()
    return render(request, 'natal.html', contexto)
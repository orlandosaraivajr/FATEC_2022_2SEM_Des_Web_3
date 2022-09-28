from asyncore import dispatcher_with_send
from django.shortcuts import render
from datetime import datetime
from .models import FeriadoModel

def verifica_feriado(request):
    hoje = datetime.today()
    resultado = FeriadoModel.objects.filter(dia=hoje.day).filter(mes=hoje.month)
    if len(resultado) > 0:
        nome_feriado = resultado[0].nome
        contexto = {'feriado': True, 'nome': nome_feriado}
        return render(request, 'feriado.html', contexto)
    else:
        contexto = {'feriado': False, 'nome': 'nenhum'}
        return render(request, 'feriado.html', contexto)
    # import ipdb ; ipdb.set_trace()

from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from fcsolutions.serializers import PessoaSerializer, FuncionarioSerializer
from fcsolutions.models import Chamado


def listaChamados(request):
    retorno = "<h1>Chamados</h1>"
    lista = Chamado.objects.all()
    for tipo in lista:
        retorno += '</br>Chamado:{}</br>'.format(lista.nome)
    return HttpResponse(retorno)

def listaChamadosbyID(request,id):
    retorno = "<h1>Chamados</h1>"
    lista = Chamado.objects.get(pk=id)
    retorno += '</br>Chamado:{}</br>'.format(lista.nome)
    return HttpResponse(retorno)


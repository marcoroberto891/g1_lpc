from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from fcsolutions.models import User, Departamento, Chamado, Categorias, Pessoa, Instituicao, Status, Funcionario

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id_pessoa', 'nome', 'cpf', 'email', 'telefone', 'usuario')

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    usuario = PessoaSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ('id_pessoa', 'nome', 'cpf', 'email', 'telefone', 'usuario', 'id_funcionario', 'id_departamento')




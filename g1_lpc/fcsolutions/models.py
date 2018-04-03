from django.db import models
from django.contrib.auth.models import User

class Instituicao(models.Model):
    id_instituicao = models.IntegerField()
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    def __str__(self):
         return '{}'.format(self.nome)

class Departamento(models.Model):
    id_departamento = models.IntegerField()
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    id_instituicao = models.ForeignKey(Instituicao, related_name='Departamento_Instituiçao', null=True, blank=False,on_delete=True)

    def __str__(self):
         return '{}'.format(self.nome)

class Pessoa(models.Model):
    id_pessoa = models.IntegerField()
    nome = models.CharField(max_length=128)
    cpf = models.CharField('cpf', max_length=11)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=10)
    usuario = models.ForeignKey(User, null=True, blank=False, on_delete=True)

    def __str__(self):

         return '{}'.format(self.nome)

class Funcionario(Pessoa):
    id_funcionario = models.ForeignKey(Pessoa, related_name='Pessoa_Funcionario', null=True, blank=False, on_delete=True)
    id_departamento = models.ForeignKey(Pessoa, related_name='Funcionario_Departamento', null=True, blank=False, on_delete=True)

    def __str__(self):
         return '{}'.format(self.nome)

class Status(models.Model):
    id_status = models.IntegerField()
    descricao = models.CharField(max_length=100)

    def __str__(self):

         return '{}'.format(self.descricao)

class Categorias(models.Model):
    id_categoria = models.IntegerField()
    descricao = models.CharField(max_length=100)

    def __str__(self):
         return '{}'.format(self.descricao)

class Chamado(models.Model):
    id_chamado = models.IntegerField()
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    id_categoria = models.ForeignKey(Categorias, related_name='chamado_categoria', null=True, blank=False,on_delete=True)
    id_status = models.ForeignKey(Status, related_name='chamado_status', null=True, blank=False,on_delete=True)
    data_abertura = models.DateField(auto_now=True)
    data_atendimento = models.DateField(auto_now=False,blank=True)
    id_funcionario_solicitante = models.ForeignKey(Pessoa, related_name='Funcionario_chamado', null=True, blank=False,on_delete=True)
    id_funcionario_solucionou = models.ForeignKey(Pessoa, related_name='Funcionarioti_chamado', null=True, blank=True,on_delete=True)

    def __str__(self):
     return '{}'.format(self.id_chamado)

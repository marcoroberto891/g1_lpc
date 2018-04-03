from django.contrib import admin
from django.contrib.auth.models import User

from fcsolutions.models import Status, Instituicao, Pessoa, Categorias, Chamado, Departamento, Funcionario

admin.site.register(Funcionario)
admin.site.register(Status)
admin.site.register(Instituicao)
admin.site.register(Pessoa)
admin.site.register(Categorias)
admin.site.register(Chamado)
admin.site.register(Departamento)
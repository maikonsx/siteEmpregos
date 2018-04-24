from django.db.models import(
	Model,
	TextField,
	ForeignKey,
)

from django.db import models

# Create your models here.

class listaEmpregos(Model):
	id = models.AutoField(primary_key=True)
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, max_length=50, null=True)
	titulo = models.TextField(max_length=100)
	descricao = TextField(null=True, blank=True)
	contato = models.TextField(max_length=100)
	salario = models.FloatField(null=True, blank=True)

	def salvar(self):
		self.save()

	def __str__(self):
		return self.titulo

class listaEmpresas(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=50)
	endereco = models.CharField(max_length=100)
	nomeEmprego = models.ForeignKey(listaEmpregos, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome

	def getId(self):
		return self.id
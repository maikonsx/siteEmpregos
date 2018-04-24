from django.db.models import(
	Model,
	TextField,
	ForeignKey,
)

from django.db import models

# Create your models here.

class listaServicos(Model):
	id = models.AutoField(primary_key=True)
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	tipo = models.CharField(max_length=200)
	text = models.TextField()
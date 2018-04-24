from django import forms
from .models import listaEmpregos

class cadastrarEmpregosForm(forms.ModelForm):

	class Meta:
		model = listaEmpregos
		fields = ('titulo', 'descricao', 'salario')


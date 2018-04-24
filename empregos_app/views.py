from django.shortcuts import render, get_object_or_404, redirect
from .models import listaEmpregos, listaEmpresas
from django.contrib.auth.decorators import login_required
from .forms import cadastrarEmpregosForm

# Create your views here.

def home(request):
	listas_empregos = listaEmpregos.objects.all()
	contexto = {'listas_empregos': listas_empregos}
	return render(request, "empregos_app/index.html", contexto)

def empresas(request):
	listas_empresas = listaEmpresas.objects.all()
	contexto_emp = {'listas_empresas': listas_empresas}
	return render(request, "empregos_app/empresas.html")

@login_required
def novo_emprego(request):
	if request.method == "POST":
		form = cadastrarEmpregosForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.save()
			return render(request, "empregos_app/index.html")
	else:
		form = cadastrarEmpregosForm()
	return render(request, "empregos_app/novo_emprego.html", {'form': form})
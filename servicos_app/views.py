from django.shortcuts import render, get_object_or_404, redirect
from .models import listaServicos
# Create your views here.

def home_servicos(request):
	listasservicos = listaServicos.objects.all()
	contexto = {'listasservicos': listasservicos}
	return render(request, "servicos_app/home_servicos.html", contexto)
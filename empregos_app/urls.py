from django.conf.urls import url

from . import views

app_name = 'empregos_app'

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^post/new/$', views.novo_emprego, name='novo_emprego'),
	url(r'^empresas/$', views.empresas, name='lista_empresas'),

]
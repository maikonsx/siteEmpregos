from django.conf.urls import url

from . import views

app_name = 'servicos_app'

urlpatterns = [
	url(r'^$', views.home_servicos, name='home_servicos'),
]
from django.conf.urls import url
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^solicitar/',solicitar,name='solicitar'),
    url(r'^espera/',  TemplateView.as_view(template_name='espera.html'), name='espera'),
    url(r'^listar/', listar_solicitacao,  name='solicitacao_list'),
    url(r'^respota/(?P<pk>[0-9]+)', Resposta, name='respota'),
    url(r'^mostra_resposta/(?P<pk>[0-9]+)', mostra_respota, name='mostra_resposta'),
    url(r'^logar/$', logar, name='logar'),
    url(r'^deslogar/$', deslogar, name='deslogar'),
]
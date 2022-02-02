from django.conf import settings
from django.contrib.auth.decorators import login_required
from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import solicitacao


class SolicitacaoForm(ModelForm):
    class Meta:
        model = solicitacao
        fields = ['nome_do_consultor','cliente','quadra',
                  'lote','data','mensagem']

class RespotaForm(ModelForm):
    class Meta:
        model = solicitacao
        fields = ['nome_do_consultor','cliente','quadra',
                  'lote','data','mensagem','status','respota']

@login_required
def solicitar(request, template_name="solicitacao.html"):
    form = SolicitacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('espera')
    return render(request,template_name,{'form':form})

@login_required
def listar_solicitacao(request, template_name="solicitacao_list.html"):
    query = request.GET.get("busca")
    ordenar = request.GET.get("ordenar", '')
    page = request.GET.get('page', '')
    if query:
        Solicitacao = solicitacao.objects.filter(nome_do_consultor__icontains=query) or solicitacao.objects.filter(id__icontains=query)
    else:
        try:
            if ordenar:
                Solicitacao = solicitacao.objects.all().order_by(ordenar)
            else:
                Solicitacao = solicitacao.objects.all()
            Solicitacao = Paginator(Solicitacao, 10)
            Solicitacao = Solicitacao.page(page)
        except PageNotAnInteger:
            Solicitacao = Solicitacao.page(1)
        except EmptyPage:
            Solicitacao = paginator.page(paginator.num_pages)
    Solicitacao = {'lista': Solicitacao}
    return render(request, template_name, Solicitacao)

@login_required
def Resposta(request, pk, template_name="resposta.html"):
    Solicitacao = get_object_or_404(solicitacao, pk=pk)
    if request.method == "POST":
        form = RespotaForm(request.POST, instance=Solicitacao)
        if form.is_valid():
            form.save()
            return redirect('solicitacao_list')
    else:
        form = RespotaForm(instance=Solicitacao)
    return render(request,template_name, {'form':form})

@login_required
def mostra_respota(request, pk,template_name="resposta_list.html"):
    Solicitacao = get_object_or_404(solicitacao, pk=pk)
    return render(request, template_name, {'Solicitacao': Solicitacao})


def logar(request, template_name="login.html"):
    next = request.GET.get('next', 'solicitacao_list')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('solicitacao_list')
            return HttpResponseRedirect(next)

        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, template_name, {'redirect_to': next})

def deslogar(request):
    logout(request)
    return redirect('logar')
    return HttpResponseRedirect(settings.LOGIN_URL)

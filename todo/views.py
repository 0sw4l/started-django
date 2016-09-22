from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView
from django.views.generic import TemplateView

from todo.forms import ConsultaForm
from todo.models import Consulta


class BaseTemplateLogin(LoginRequiredMixin, ListView):
    pass


class HomeView(BaseTemplateLogin):
    model = Consulta
    template_name = 'home.html'


@login_required
def crear_consulta(request):
    form = ConsultaForm(
        request.POST or None
    )
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'form.html', context)


def modificar_consulta(request, **kwargs):
    id = kwargs.get('pk')
    consulta = Consulta.objects.get(id=id)
    form = ConsultaForm(
        request.POST or None,
        instance=consulta
    )
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'form.html', context)


def eliminar_consulta(request, **kwargs):
    id = kwargs.get('pk')
    consulta = Consulta.objects.get(id=id)
    consulta.delete()
    return redirect('home')
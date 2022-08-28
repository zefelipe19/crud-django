from operator import concat
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Contact


# Create your views here.
class VerContatos(ListView):
    model = Contact
    queryset = Contact.objects.all()
    template_name = 'contacts/index.html'
    context_object_name = 'Contatos'


class CriarContato(CreateView):
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('ver_contatos')
    template_name = 'contacts/criar_contato.html'


class AtualizarContato(UpdateView):
    model = Contact
    fields = '__all__'
    success_url = reverse_lazy('ver_contatos')
    template_name = 'contacts/criar_contato.html'


class VerContato(DetailView):
    queryset = Contact.objects.all()
    context_object_name = 'Contato'
    template_name = 'contacts/ver_contato.html'


class DeletarContato(DeleteView):
    queryset = Contact.objects.all()
    context_object_name = 'Contato'
    template_name = 'contacts/deletar_contato.html'
    success_url = reverse_lazy('ver_contatos')

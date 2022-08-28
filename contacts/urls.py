from django.urls import path
from .views import VerContato, VerContatos, CriarContato, AtualizarContato, DeletarContato


urlpatterns = [
    path('', VerContatos.as_view(), name='ver_contatos'),
    path('criar', CriarContato.as_view(), name='criar_contato'),
    path('atualizar/<int:pk>/', AtualizarContato.as_view(), name='atualizar_contato'),
    path('contato/<int:pk>/', VerContato.as_view(), name='ver_contato'),
    path('deletar/<int:pk>/', DeletarContato.as_view(), name='deletar_contato')
]

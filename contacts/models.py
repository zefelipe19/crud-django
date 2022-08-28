from django.db import models

# Create your models here.
class Contact(models.Model):
    nome = models.TextField(max_length=80, verbose_name='Nome')
    idade = models.IntegerField()
    telefone = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

from django.db import models

# Create your models here.

class User(models.Model):
    Usuario = models.CharField(max_length=30)
    Senha = models.DecimalField(max_digits=5, decimal_places=2)
    Nome = models.CharField(max_length=30)
    Endereco = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Celular = models.CharField(max_length=30)
    AvaliacaoEmpresa = models.TextField()

def __str__(self):
    return self.Usuario + ' ' + self.Senha   
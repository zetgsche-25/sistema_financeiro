from django.db import models

class Lancamento(models.Model):
    TIPO_CHOICES = [
        ('R', 'Receita'),
        ('D', 'Despesa'),
    ]

    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - {self.valor}"

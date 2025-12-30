from django.shortcuts import render
from .models import Lancamento
from django.db.models import Sum

def home(request):
    receitas = Lancamento.objects.filter(tipo='R').aggregate(total=Sum('valor'))['total'] or 0
    despesas = Lancamento.objects.filter(tipo='D').aggregate(total=Sum('valor'))['total'] or 0
    saldo = receitas - despesas

    lancamentos = Lancamento.objects.all().order_by('-data')

    context = {
        'receitas': receitas,
        'despesas': despesas,
        'saldo': saldo,
        'lancamentos': lancamentos
    }

    return render(request, 'financas/home.html', context)

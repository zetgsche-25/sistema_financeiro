receitas = []
despesas = []

def adicionar_receita(valor, descricao):
    receitas.append({"valor": valor, "descricao": descricao})

def adicionar_despesa(valor, descricao):
    despesas.append({"valor": valor, "descricao": descricao})

def calcular_saldo():
    total_receitas = sum(r["valor"] for r in receitas)
    total_despesas = sum(d["valor"] for d in despesas)
    return total_receitas - total_despesas

def listar_lancamentos():
    print("\n📥 Receitas:")
    for r in receitas:
        print(f"- {r['descricao']}: R$ {r['valor']}")

    print("\n📤 Despesas:")
    for d in despesas:
        print(f"- {d['descricao']}: R$ {d['valor']}")

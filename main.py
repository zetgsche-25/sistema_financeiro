from financeiro import (
    adicionar_receita,
    adicionar_despesa,
    calcular_saldo,
    listar_lancamentos
)
from utils import menu

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor da receita: "))
        descricao = input("Descrição: ")
        adicionar_receita(valor, descricao)
        print("✅ Receita adicionada!")

    elif opcao == "2":
        valor = float(input("Valor da despesa: "))
        descricao = input("Descrição: ")
        adicionar_despesa(valor, descricao)
        print("✅ Despesa adicionada!")

    elif opcao == "3":
        saldo = calcular_saldo()
        print(f"💰 Saldo atual: R$ {saldo}")

    elif opcao == "4":
        listar_lancamentos()

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("❌ Opção inválida!")

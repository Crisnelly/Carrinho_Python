#Dicionário
#Caixa de supermercado
tabela = {"Alface": 5.00,
          "Batata": 4.55,
          "Tomate": 9.80,
          "Feijão": 7.30}

estoque= {"Alface": 10,
          "Batata": 15,
          "Tomate": 7,
          "Feijão": 20}
valor_total = 0
while True:
    produto = input("Qual o produto? ").capitalize()
   
    if produto == "Sair":
        print("Bye!")
        break

    if produto not in tabela:
        print("Produto não encontrado.")
        continue

    if produto not in estoque:
        print("Produto sem estoque.")
        continue

    quantidade = int(input("Quantidade:"))
    if quantidade > estoque[produto]:
        print(f"Desculpe, só temos {estoque[produto]} unidades em estoque.")
        continue

    valor_produto = tabela[produto] * quantidade
    valor_total = valor_total + valor_produto
    print(f"{quantidade}- {estoque} comprados por R${valor_produto:.2f}")
    estoque[produto] -= quantidade
    print(f"Estoque restante de {produto}: {estoque[produto]} unidades")

print(f"Valor total das compras foi de: R${valor_total:.2f}")


nomedoproduto = str(input('digite o nome do produto: '))
valordoproduto = float(input('digite o valor do produto:  '))
quantidadedoproduto = int(input('digite a quantidade: '))

valordacompra = (valordoproduto*quantidadedoproduto)

print(f'Voce acaba de comprar {quantidadedoproduto} {nomedoproduto} por {valordoproduto} reais cada, sendo o total da compra de {valordacompra}reais')
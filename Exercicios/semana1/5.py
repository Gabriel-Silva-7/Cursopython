nomedoproduto = str(input('digite o nome do produto: '))
valordoproduto = float(input('digite o valor do produto:  '))
quantidadedoproduto = int(input('digite a quantidade: '))

valordacompra = (valordoproduto*quantidadedoproduto)

print(f'Voce acaba de comprar {quantidadedoproduto} {nomedoproduto} por {valordoproduto} reais cada, sendo o total da compra de {valordacompra} reais')

valordacompracomdesconto = ((valordacompra/100)*85)

print(f'sendo que voce comprando avista recebe um desconto de 15% o valor passsando a ser {valordacompracomdesconto}')
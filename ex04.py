#Faça um programa que lê o nome de um produto, a quantidade comprada, o valor
#unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na
#tela o nome do produto e o valor total da venda.

produto = 'Geladeira'
quantidadeComprada = 2
valorUnitario = 1200
percentualDesconto = 5

valorSemDesconto = valorUnitario * quantidadeComprada
valorDesconto = (percentualDesconto / 100) * valorSemDesconto
valorTotalVenda = valorSemDesconto - valorDesconto

print('Produto: ' + produto + ' Valor: ' + str(valorTotalVenda))
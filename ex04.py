#Faça um programa que lê o nome de um produto, a quantidade comprada, o valor
#unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na
#tela o nome do produto e o valor total da venda.

class total:
    def __init__ (self):
        self.produto = input("Insira o produto que você comprou: ")
        self.quantidadeComprada = int(input("Insira a quantidade que você comprou: "))
        self.valorUnitario = int(input("Qual o valor unitário do produto: "))
        self.percentualDesconto = int(input("Qual o percentual de desconto: "))

    def iniciar(self):
        self.calculaValorVenda()

    def calculaValorVenda(self):
        valorSemDesconto = self.valorUnitario * self.quantidadeComprada
        valorDesconto = (self.percentualDesconto / 100) * valorSemDesconto
        valorTotalVenda = valorSemDesconto - valorDesconto

        print(f'Produto: {self.produto} Valor total da venda: {valorTotalVenda}')

total = total()
total.iniciar()
#Faça um programa que lê o nome de um produto, a quantidade comprada, o valor
#unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na
#tela o nome do produto e o valor total da venda.

class Total:
    def __init__ (self):
        self.produto = input("Insira o produto que você comprou: ")
        self.quantidade_comprada = int(input("Insira a quantidade que você comprou: "))
        self.valor_unitario = int(input("Qual o valor unitário do produto: "))
        self.percentual_desconto = int(input("Qual o percentual de desconto: "))

    def iniciar(self):
        self.calculaValorVenda()

    def calculaValorVenda(self):
        valor_sem_desconto = self.valor_unitario * self.quantidade_comprada
        valor_desconto = (self.percentual_desconto / 100) * valor_sem_desconto
        valor_total_venda = valor_sem_desconto - valor_desconto

        print(f'Produto: {self.produto} Valor total da venda: {valor_total_venda}')

total = Total()
total.iniciar()
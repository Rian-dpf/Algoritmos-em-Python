#Faça um programa que lê um valor em reais e calcule o valor equivalente em dólares.
#O usuário deve informar, além do valor em reais da compra, o valor da cotação do
#dólar.

class Conversor:
  def __init__(self):
    self.valor_reais = float(input("Digite o valor em reais: "))
    self.cotacao_dolar = float(input("Qual a cotação atual do dólar: "))

  def iniciar(self):
    self.calculaDolar()

  def calculaDolar(self):
    valor_em_dolar = self.valor_reais / self.cotacao_dolar

    print('O valor em dólar é: %.2f' % valor_em_dolar)

conversor = Conversor()
conversor.iniciar()
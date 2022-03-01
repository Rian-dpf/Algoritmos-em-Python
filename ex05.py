#Faça um programa que lê um valor em reais e calcule o valor equivalente em dólares.
#O usuário deve informar, além do valor em reais da compra, o valor da cotação do
#dólar.

class conversor:
  def __init__(self):
    self.valorReais = float(input("Digite o valor em reais: "))
    self.cotacaoDolar = float(input("Qual a cotação atual do dólar: "))

  def iniciar(self):
    self.calculaDolar()

  def calculaDolar(self):
    valorEmDolar = self.valorReais * self.cotacaoDolar

    print("O valor em dólar é: " + str(valorEmDolar))

conversor = conversor()
conversor.iniciar()
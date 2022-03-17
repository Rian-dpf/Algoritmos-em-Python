#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
#informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
#ordem lida.

class ApresentaNaOrdemIversa:
  def __init__ (self):
    self.idades = []
    self.alturas = []

  def iniciar(self):
    self.ordenaEApresenta()

  def ordenaEApresenta(self):
    for i in range(1,6):

      print(f"{i}º Pessoa")
      
      idade = int(input("Digite a sua idade: "))
      altura = float(input("Digite a sua altura: "))

      self.idades.append(idade)
      self.alturas.append(altura)

      print("Ordem Inversa:")
      print(self.idades[::-1])
      print(self.alturas[::-1])

apresentaNaOrdemIversa = ApresentaNaOrdemIversa()
apresentaNaOrdemIversa.iniciar()
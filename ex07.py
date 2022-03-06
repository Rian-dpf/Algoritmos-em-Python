#Faça um programa que dada duas strings, s1 e s2 retornam uma nova string composta
#do primeiro, do meio e do último caracteres de cada string de entrada.

class NovaString:
  def __init__ (self):
    self.s1 = str(input("Digite uma string: "))
    self.s2 = str(input("Digite outra string: "))

  def iniciar(self):
    self.criaNovaString()
  
  def criaNovaString(self):
    teste = enumerate(self.s1)
    
    print(teste)

novaString = NovaString()
novaString.iniciar()
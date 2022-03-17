#Faça um programa que dada duas strings, s1 e s2 retornam uma nova string composta
#do primeiro, do meio e do último caracteres de cada string de entrada.

class NovaString:
  def __init__ (self):
    self.s1 = str(input("Digite uma string: "))
    self.s2 = str(input("Digite outra string: "))

  def iniciar(self):
    self.criaNovaString()
  
  def criaNovaString(self):
    tamanho_s1 = len(self.s1)
    tamanho_s2 = len(self.s2)

    s3 = self.s1[0] + self.s1[round(tamanho_s1 / 2)] + self.s1[-1] + self.s2[0] + self.s2[round(tamanho_s2 / 2)] + self.s2[-1]

    print(s3)

novaString = NovaString()
novaString.iniciar()
#Faça um programa que dada duas strings, s1 e s2 retornam uma nova string composta
#do primeiro, do meio e do último caracteres de cada string de entrada.

class novaString:
  def _init_ (self):
    self.s1 = str(input("Digite uma string: "))
    self.s2 = str(input("Digite outra string: "))

  def iniciar(self):
    self.criaNovaString()
  
  def criaNovaString(self):
    s3 = self.s1[0]

    print(s3)

novaString = novaString()
novaString.iniciar()
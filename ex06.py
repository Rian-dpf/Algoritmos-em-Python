#Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em
#maiúscula e sem espaços em branco.

class conversorFrase:
  def __init__ (self):
    self.frase = str(input("Digite uma frase qualquer: "))

  def iniciar(self):
    self.converteFrase()

  def converteFrase(self):
    fraseMaiusculaSemEspacos = self.frase.upper().replace(" ", "")

    print(fraseMaiusculaSemEspacos)

conversorFrase = conversorFrase()
conversorFrase.iniciar()
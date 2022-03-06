#Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em
#maiúscula e sem espaços em branco.

class ConversorFrase:
  def __init__ (self):
    self.frase = str(input("Digite uma frase qualquer: "))

  def iniciar(self):
    self.converteFrase()

  def converteFrase(self):
    frase_maiuscula_sem_espacos = self.frase.upper().replace(" ", "")

    print(frase_maiuscula_sem_espacos)

conversorFrase = ConversorFrase()
conversorFrase.iniciar()
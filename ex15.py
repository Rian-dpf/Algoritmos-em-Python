#Crie um Python Script que conte quantas vezes um nome está presente em uma lista
#[’nome1’, ’nome2’, ...] e armazena essa contagem em um dicionário {’nome’: xvezes}.

import collections

class Contador:
  def __init__ (self):
    self.nomes_lista = ["Rian", "Guilherme", "Matheus", "Rian", "Moacir", "Matheus"]

  def iniciar(self):
      self.ContaVezes()

  def ContaVezes(self):
      conta_vezes = collections.Counter(self.nomes_lista)

      print(conta_vezes)

contador = Contador()
contador.iniciar()            
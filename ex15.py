#Crie um Python Script que conte quantas vezes um nome está presente em uma lista
#[’nome1’, ’nome2’, ...] e armazena essa contagem em um dicionário {’nome’: xvezes}.

class Contador:
  def __init__ (self):
    self.nomes_lista = ["Rian", "Guilherme", "Matheus", "Rian", "Moacir", "Matheus"]

  def iniciar(self):
      self.ContaVezes()

  def ContaVezes(self):
      teste = {self.nomes_lista[i]: len(self.nomes_lista[i]) for i in range(len(self.nomes_lista))}

      print(teste)

contador = Contador()
contador.iniciar()
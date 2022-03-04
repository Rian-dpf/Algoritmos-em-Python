#Crie um Python Script que conte quantas vezes um nome está presente em uma lista
#[’nome1’, ’nome2’, ...] e armazena essa contagem em um dicionário {’nome’: xvezes}.

class contador:
  def _init_ (self):
    self.nomes = ["Rian", "Guilherme", "Matheus", "Rian", "Moacir", "Matheus"]

  def iniciar(self):
      self.ContaVezes()

  def ContaVezes(self):
      for i in self.nomes:
        print(i)

contador = contador()
contador.iniciar()
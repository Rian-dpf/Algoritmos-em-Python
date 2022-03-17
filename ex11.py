#Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua
#posição na lista.

class MostraPosicao:
  def __init__ (self):
    self.lista = [5,4,8,9,7]

  def iniciar(self):
    self.verificaPosicao()

  def verificaPosicao(self):
    for i in range(0, len(self.lista)):
      print(f'{self.lista[i]} : {i}')

mostraPosicao = MostraPosicao()
mostraPosicao.iniciar()
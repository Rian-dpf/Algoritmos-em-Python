#Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua
#posição na lista.

class mostraPosicao:
  def __init__ (self):
    self.lista = [5,4,8,9,7]

  def iniciar(self):
    self.verificaPosicao()

  def verificaPosicao(self):
    teste = list(range(len(self.lista)))
    numeroTeste = int
    indiceTeste = int

    for numero in self.lista:
      numeroTeste = numero

    for indice in teste:      
      indiceTeste = indice
      
      print(f"{numeroTeste} : {indiceTeste}")

      

mostraPosicao = mostraPosicao()
mostraPosicao.iniciar()
#Dadas duas listas L1 e L2, com n valores inteiros, respectivamente, escreva um
#programa que concatene as listas L1 e L2 em uma nova lista L3. Em seguida, imprima
#a lista L3 ordenada de maneira crescente e decrescente.

class ordena:
  def __init__ (self):
    self.l1 = [12,87,65,90]
    self.l2 = [56,786,89,34,9]

  def iniciar(self):
    self.ordenaCrescente()
    self.ordenaDecrescente()
    
  def ordenaCrescente(self):
    l3 = self.l1 + self.l2
    
    l3.sort()

    print(l3)

  def ordenaDecrescente(self):
    l3 = self.l1 + self.l2
    
    l3.sort(reverse=True)

    print(l3)

ordena = ordena()
ordena.iniciar()
#Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule e 
#imprima o valor de z

class descobreValor:
    def __init__ (self):
        self.x = int(input("Digite o valor de X: "))
        self.y = int(input("Digite o valor de y: "))

    def iniciar(self):
        self.calculaZ()

    def calculaZ(self):
        z = (self.x * self.x + self.y * self.y) / self.x - self.y

        print(z)

descobreValor = descobreValor()
descobreValor.iniciar()
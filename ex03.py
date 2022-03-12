#Faça um Programa que leia 4 notas, mostre as notas e a média na tela

class Media:
    def __init__ (self):
        self.nota1 = float(input("Qual a sua nota 1: "))
        self.nota2 = float(input("Qual a sua nota 2: "))
        self.nota3 = float(input("Qual a sua nota 3: "))
        self.nota4 = float(input("Qual a sua nota 4: "))

    def iniciar(self):
        self.calculaMedia()

    def calculaMedia(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

        print(f'O valor de cada nota é {self.nota1}, {self.nota2}, {self.nota3}, {self.nota4}')
        print(f'A média é: {media}')

media = Media()
media.iniciar()
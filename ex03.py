#Faça um Programa que leia 4 notas, mostre as notas e a média na tela

class media:
    def __init__ (self):
        self.nota1 = int(input("Qual a sua primeira nota 1: "))
        self.nota2 = int(input("Qual a sua primeira nota 2: "))
        self.nota3 = int(input("Qual a sua primeira nota 3: "))
        self.nota4 = int(input("Qual a sua primeira nota 4: "))

    def iniciar(self):
        self.calculaMedia()

    def calculaMedia(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

        print(media)

media = media()
media.iniciar()
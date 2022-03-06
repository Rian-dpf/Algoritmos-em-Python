#Faça um Programa que leia 4 notas, mostre as notas e a média na tela

class Media:
    def __init__ (self):
        self.nota_1 = int(input("Qual a sua primeira nota 1: "))
        self.nota_2 = int(input("Qual a sua primeira nota 2: "))
        self.nota_3 = int(input("Qual a sua primeira nota 3: "))
        self.nota_4 = int(input("Qual a sua primeira nota 4: "))

    def iniciar(self):
        self.calculaMedia()

    def calculaMedia(self):
        media = (self.nota_1 + self.nota_2 + self.nota_3 + self.nota_4) / 4

        print(f'Média final: {media}')

media = Media()
media.iniciar()
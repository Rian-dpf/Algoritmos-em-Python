#2. Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

class Media:
    def __init__ (self):
        self.notas = [10,9,8,9]

    def iniciar(self):
        self.calculaMedia()

    def calculaMedia(self):
        media_final = sum(self.notas) / 4

        print(media_final)

Media = Media()
Media.iniciar()
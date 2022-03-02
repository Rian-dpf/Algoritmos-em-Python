#Escreva um programa para verificar se a palavra 'laranja' está presente em "Isto é suco
#de laranja".

class existePalavra:
    def __init__ (self):
        self.frase = "Isto é suco de laranja"
        self.palavra = "laranja"

    def iniciar(self):
        self.verificaPalavra()

    def verificaPalavra(self):
        if self.palavra not in self.frase:
            print(f"A palavra {self.palavra} não está presente na frase {self.frase}")
        else:
            print(f"A palavra {self.palavra} está presente na frase {self.frase}")

existePalavra = existePalavra()
existePalavra.iniciar()
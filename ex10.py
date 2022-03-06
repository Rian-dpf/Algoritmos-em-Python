#Crie um programa que imprima o comprimento de uma string fornecida pelo usuário.

class ComprimentoString:
    def __init__ (self):
        self.string = input("Coloque uma string qualquer: ")

    def iniciar(self):
        self.verificaComprimentoString()

    def verificaComprimentoString(self):
        print(f'O comprimento da string {self.string} é: {len(self.string)}')

ComprimentoString = ComprimentoString()
ComprimentoString.iniciar()
#Faça um programa que leia dois valores numéricos e realize a soma, subtração,
#multiplicação e divisão deles.

class Calculadora:
    def __init__ (self):
        self.numero_1 = int(input("Digite um número: "))
        self.numero_2 = int(input("Digite outro número: "))

    def iniciar(self):
            self.soma()
            self.subtracao()
            self.multiplicacao()
            self.divisao()

    def soma(self):
        soma = self.numero_1 + self.numero_2

        print(f"A soma é: {soma}")

    def subtracao(self):
        sub = self.numero_1 - self.numero_2

        print(f"A subtração é: {sub}")

    def multiplicacao(self):
        mult = self.numero_1 * self.numero_2

        print(f"A multiplicação é: {mult}")

    def divisao(self):
        div = self.numero_1 / self.numero_2

        print(f"A divisão é: {div}")

calculadora = Calculadora()
calculadora.iniciar()
#Escreva um programa que receba o salário de um funcionário (float), e retorne o
#resultado do novo salário com reajuste de 35%

class reajusteSalarial:
    def __init__ (self):
        self.salarioAtual = float(input("Digite o seu salário atual: "))
        self.porcentagemReajuste = 35
        
    def iniciar(self):
        self.calculaReajuste()

    def calculaReajuste(self):
        reajuste = (self.porcentagemReajuste / 100) * self.salarioAtual
        salarioReajustado = self.salarioAtual + reajuste

        print('O seu novo salário com um reajuste de 35% é: ' + str(salarioReajustado))

reajusteSalarial = reajusteSalarial()
reajusteSalarial.iniciar()
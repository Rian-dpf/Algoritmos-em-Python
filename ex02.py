#Escreva um programa que receba o salário de um funcionário (float), e retorne o
#resultado do novo salário com reajuste de 35%

class ReajusteSalarial:
    def __init__ (self):
        self.salario_atual = float(input("Digite o seu salário atual: "))
        self.porcentagem_reajuste = 35
        
    def iniciar(self):
        self.calculaReajuste()

    def calculaReajuste(self):
        reajuste = (self.porcentagem_reajuste / 100) * self.salario_atual
        salario_reajustado = self.salario_atual + reajuste

        print(f'O seu novo salário com um reajuste de 35% é: {salario_reajustado}')

reajusteSalarial = ReajusteSalarial()
reajusteSalarial.iniciar()
# Crie um programa que cadastre informações de uma pessoa (nome, idade e cpf) e
# depois coloque em um dicionário. Depois o usuário poderá escolher alguma das
# informações para acessa-la.

class Cadastro:
    def __init__ (self):
      self.dados = {
          'Nome': str,
          'Idade': int,
          'cpf': str
      }

    def iniciar(self):
      self.cadastraInformacoesPessoa()
      self.acessaInformacaoPessoa()
    
    def cadastraInformacoesPessoa(self):
      for x in self.dados:
        if x == 'Nome':
          self.dados[x] = str(input("Digite o seu nome: "))
        elif x == 'Idade':
          self.dados[x] = int(input("Digite a sua idade: "))
        else:
          self.dados[x] = str(input("Digite o seu cpf: "))

    def acessaInformacaoPessoa(self):
      print("Qual informação você deseja acessar? ")

      print("1 - Nome")
      print("2 - Idade")
      print("3 - cpf")

      opcao = int(input("Digite a opção de sejada: "))

      if opcao == 1:
        print(self.dados.get('Nome'))

      elif opcao == 2:
        print(self.dados.get('Idade'))

      elif opcao == 3:
        print(self.dados.get('cpf'))

      else:
        print('Digite uma opção válida!')

Cadastro = Cadastro()
Cadastro.iniciar()
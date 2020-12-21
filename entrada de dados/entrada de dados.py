nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

ano_atual = 2020
nascimento = ano_atual - int(idade)
soma = (num1 + num2)

print(f'{nome} tem {idade} anos.\n'
      f'{nome} nasceu em {nascimento}.\n'
      f'Resultado da soma: {soma}.')


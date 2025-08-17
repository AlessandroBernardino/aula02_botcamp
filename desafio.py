CONSTANTE_BONUS = 1000

#Solicita ao usuário que digite o nome
nome_usuario = input("Digite o seu nome: ")
if nome_usuario.isdigit():
  print("Você digitou o nome errado.")
  exit()
elif len(nome_usuario) == 0:
  print("Você não digitou nada")
  exit()
elif nome_usuario.isspace():
  print("Você só digitou espaço")
  exit()
#Solicita ao usuário que digite o valor do salário
salario_usuario = float(input("Digite o seu salário: "))

#Solicita ao usuário que digite o valor do bonus recebido
bonus_recebido = float(input("Digite o seu bonus: "))

#calcula o valor do bônus final
valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_recebido                    
print(f"O valor total do bonus é {valor_bonus}")                      
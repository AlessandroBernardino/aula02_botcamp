#programa que pede dois números inteiros e imprime a divisão inteira do primeiro pelo segundo
import math

""" numero_01 = int(input('Insira um numero inteiro: '))
numero_02 = int(input('Insira um numero inteiro: '))
resultado = numero_01 // numero_02
print(resultado) """

#programa para calcular a área de um circulo
""" raio_circulo = float(input("Insira o raio: "))
area_circulo =  math.pi * raio_circulo**2
print(f"a área é: {area_circulo:.2f}") """

#verificando se um número é um inteiro
numero = input("Insira um número: ")
if isinstance(numero,int):
  print("o número é inteiro")
else:
  print('o número não é inteiro')
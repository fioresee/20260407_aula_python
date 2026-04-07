#EX1
# nota1 = float(input("Escreva a primeira nota: "))
# nota2 = float(input("Escreva a segunda nota: "))
# nota3  = float(input("Escreva a terceira nota: "))
# media = (nota1 + nota2 + nota3) / 3
# print(f"A sua média é {media:.1f}")
#
# if media >= 6:
#     print("Você foi aprovado!")
# else:
#     print("Você foi reprovado!")

#EX2

# numero_inteiro = int(input("Digite um número inteiro: "))
# if numero_inteiro % 2 == 0:
#     print("O número é par!")
# else:
#     print("O número é impar!")

#EX3
#
# numero = int(input("Digite um número inteiro: "))
# if numero < 0:
#     numero = numero * (-1)
#     print(numero)
# else:
#     print(numero)

# EX4

letra = input("Digite uma letra: ").lower()
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("É uma vogal")
else:
    print("É uma consoante")

# #EXERCÍCIO 5
# # num = int(input('digite um numero: '))
# #
# # if num > 0:
# #     print('o numero é positivo')
# # elif num < 0:
# #     print('negativo')
# # elif num == 0:
# #     print('zero')
# # else:
# #     print('número inválido')

#EX6
#
# hora1 = int(input("Digite um número: "))
# min = int(input("Digite outro número: "))
#
# if hora1 > 23 or min > 59:
#     print("Hora inválida")
# else:
#     print(f"{hora1}:{min}")

#EX7
#
# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite um número: "))
# maior = numero1
#
# if numero2 > numero1:
#     numero2 = maior
#     print(f"O maior número é {maior}!")
#
# elif numero1 == numero2:
#     print("Os números são iguais!")

#EX8
#
# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite um número: "))
# numero3 = int(input("Digite um número: "))
#
# if numero1 < numero2 and numero1 < numero3:
#     print(f"O número {numero1} é menor")
# elif numero2 < numero1 and numero2 < numero3:
#     print(f"O número {numero2} é menor")
# elif numero3 < numero1 and numero3 < numero2:
#     print(f"O número {numero3} é menor")
# elif numero1 == numero2 and numero2 == numero3 and numero1 == numero3:
#     print("Os números são iguais!")

#EX9
#
# valor1 = int(input("digite um número:"))
# valor2 = int(input("digite um número:"))
# valor3 = int(input("digite um número:"))
#
# if valor1 == valor2 and valor2 == valor3 and valor1 == valor3:
#     print("Os lados do triãngulo são iguais. portanto é um triangulo equilátero!")
# elif valor1 == valor2 or valor2 == valor3 or valor1 == valor3:
#     print("O triangulo possui 2 lados iguais. portanto o triangulo é isósceles")
# elif valor1 != valor2 and valor2 != valor3 and valor1 != valor3:
#     print("O triangulo não possui lados iguais. Portanto o triangulo é escaleno")

#EX10

# salario_fixo = float(input("Digite seu salário fixo: "))
# valor_vendas = float(input("Digite o valor das vendas efetuadas: "))
#
# if valor_vendas <= 1500:
#     comissao = valor_vendas * 0.03
# elif valor_vendas > 1500:
#     valor_passado = valor_vendas - 1500
#
#     comissao = valor_passado * 0.05
# salariototal = comissao + salario_fixo
#
# print(f"salário total: R$ {salariototal:.2f}")
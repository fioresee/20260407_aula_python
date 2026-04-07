numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
escolha = float(input("Escolha a operação que deseja fazer: "))

match escolha:
    case 1:
        soma = numero1 + numero2
        print(f"A soma é {soma}.")
    case 2:
        sub = numero1 - numero2
        print(f"A subtração é {sub}.")
    case 3:
        mult = numero1 * numero2
        print(f"A multiplicação é {mult}.")
    case 4:
        div = numero1 / numero2
        print(f"A divisão é {div}.")


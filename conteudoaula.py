titulo = "Dia da Semana"
print(f"{titulo:^30}")
numero = int(input("Escolha um número de 1 até 7: "))

#abordagem de match case
match numero:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sábado")
    case 8:
        print("Número inválido!")


# EX4

letra = input("Digite uma letra: ").lower()
match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("É uma vogal!")
    case _:
        print("É uma consoante!")
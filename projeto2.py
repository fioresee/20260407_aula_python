#Estrutura de Decisão
#if, then(:), else:
#igualdades (==) e desigualdades (>, <, >=, <=, !=)
#operadores lógicos - juntam duas ou mais comparações no mesmo if
#and (malvado), or (bonzinho), not (do contra)
#elif - nada mais é que a junção do else+if

titulo = "Dia da Semana"
print(f"{titulo:^30}")
numero = int(input("Escolha um número de 1 até 7: "))

#abordagem de elifs aninhados
if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-Feira")
elif numero == 3:
    print("Terça-Feira")
elif numero == 4:
    print("Quarta-Feira")
elif numero == 5:
    print("Quinta-Feira")
elif numero == 6:
    print("Sexta-Feira")
elif numero == 7:
    print("Sábado")
else:
    print("Número inválido!")
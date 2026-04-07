#Estrutura de Decisão
#if, then(:), else:
#igualdades (==) e desigualdades (>, <, >=, <=, !=)
#operadores lógicos - juntam duas ou mais comparações no mesmo if
#and (malvado), or (bonzinho), not (do contra)
#elif - nada mais é que a junção do else+if

titulo = "Dia da Semana"
print(f"{titulo:^30}")
numero = int(input("Escolha um número de 1 até 7: "))

#abordagem de números aninhados
if numero == 1: #como estamos comparando com igualdades,
    # tanto faz comparar com o 1(domingo) primeiro
    #como com o 5(quinta)
    #é particularmente utilizar o número mais escolhido
    print("Domingo")
else:
    if numero == 2:
        print("Segunda-Feira")
    else:
        if numero == 3:
            print("Terça-Feira")
        else:
            if numero == 4:
                print("Quarta-Feira")
            else:
                if numero == 5:
                    print("Quinta-Feira")
                else:
                    if numero == 6:
                        print("Sexta-Feira")
                    else:
                        if numero == 7:
                            print("Sábado")
                        else:
                            print("Número inválido!")

        #case
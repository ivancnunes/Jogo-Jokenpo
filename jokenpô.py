import random
import time
vitoria = derrotas = empates = 0
while True:
    time.sleep(1)
    print("\nVAMOS COMEÇAR O JOGO!\n")
    print("-"*20)
    opcao= int(input("ESCOLHA:\n" \
    "[1] PEDRA\n" \
    "[2] PAPEL\n" \
    "[3] TESOURA\n" \
    "Opção: "))
    print("-"*20)
    pc= ["PEDRA", "PAPEL", "TESOURA"]
    pc= random.choice(pc)
    time.sleep(1)
    # EMPATES
    if (opcao == 1 and pc == "pedra") or \
    (opcao == 2 and pc == "papel") or \
    (opcao == 3 and pc == "tesoura"):
        print(f"você e o pc jogaram a mesma opção {pc}\n"
        f"Tivemos um empate!")
        empates +=1
    # DERROTAS
    elif (opcao == 1 and pc == "PAPEL") or \
        ( opcao == 2 and pc == "TESOURA") or \
        (opcao == 3 and pc == "PEDRA"):
        print(f"O pc escolheu {pc}")
        print("você perdeu")
        derrotas +=1

    # VITORIAS
    elif (opcao == 2 and pc == "PEDRA") or \
        (opcao == 3 and pc == "PAPEL") or \
        ( opcao == 1 and pc == "TESOURA") :
        print(f"O pc escolheu {pc}")
        print("você ganhou")
        vitoria +=1
    
    elif opcao not in [1,2,3]:
        print("Opação invalida, tente novamente!")

    continuar = str(input("\nDeseja jogar novamente? (S|N) ")).lower()
    if continuar in ["não", "n"]:
        print("-"*20)
        print("Jogo finalizado!")
        print("-"*20)
        print(f"Total de vitorias: {vitoria}\n"
            f"Total de derrotas: {derrotas}\n"
            f"Total de empates: {empates}")
        break
    time.sleep(1)
    print("-"*20)
    print("\nVAMOS NOVAMENTE\n")
    print("-"*20)
from src.utils import clear

def menu_de_operacoes():
    clear()
    print("Digite o número da operação desejada:")
    print("1 - Achar um pokemon específico através do nome.")
    print("2 - Dado o nome de um determinado tipo, retornar os pokemons feitos do mesmo.")
    print("3 - Retornar todos os pokemon lendários.")
    print("4 - Retornar todos os pokemons que tem mega evolução.")
    print("5 - Retornar todos os pokemons que tem gênero.")
    print("6 - Retornar todos os pokemons por ordem crescente de id.")
    print("7 - Retornar todos os pokemons por ordem decrescente de id.")
    print("9 - Sair")
    operation = -1
    while operation == -1:
        try:
            operation = int(input())
            if operation > 10 or operation < 0:
                print("Operação inválida!\n")
                operation = -1
        except:
            print("Operação inválida!\n")
    return operation

def menu_nova_operacao():
    print("Deseja fazer uma nova operação? 1 - Sim, 0 - Não")
    operation = -1
    while operation == -1:
        try:
            operation = int(input())
            if operation > 10 or operation < 0:
                print("Opção inválida!\n")
                operation = -1
        except:
            print("Opção inválida!\n")
    return operation
from src.utils import clear
import struct

def menu_de_operacoes():
    clear()
    print("\nDigite o número da operação desejada:")
    print("1 - Pesquisar Pokémon pelo Nome")
    print("2 - Listar todos os Pokémons de um Tipo")
    print("3 - Listar todos os Pokémons Lendários")
    print("4 - Listar todos os Pokémons com Mega Evolução")
    print("5 - Listar todos os Pokémons com Gênero")
    print("6 - Listar todos os pokemons em ordem crescente de ID")
    print("7 - Retornar todos os pokemons em ordem decrescente de ID")
    print("8 - Adicionar novo Pokémon")
    print("9 - Remover Pokemon")
    print("10 - Sair")
    operation = -1
    while operation == -1:
        try:
            operation = int(input())
            if operation > 10 or operation < 0:
                print("\nOperação inválida!\n")
                operation = -1
        except:
            print("\nOperação inválida!\n")
    return operation

def menu_nova_operacao():
    print("\nDeseja fazer uma nova operação? 1 - Sim, 0 - Não")
    operation = -1
    while operation == -1:
        try:
            operation = int(input())
            if operation > 10 or operation < 0:
                print("\nOpção inválida!\n")
                operation = -1
        except:
            print("\nOpção inválida!\n")
    return operation


def menu_de_criacao_arquivos():
    print("\nDeseja refazer a base de dados? 1 - Sim, 0 - Não")
    operation = -1
    while operation == -1:
        try:
            operation = int(input())
            if operation > 10 or operation < 0:
                print("\nOpção inválida!\n")
                operation = -1
        except:
            print("\nOpção inválida!\n")
    return operation
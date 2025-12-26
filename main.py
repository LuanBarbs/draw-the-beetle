from minimax import expectiminimax, expectiminimax_ab
from beetle_game import is_terminal
from tree_visualizer import print_tree

INITIAL_STATE = [0, 0, 0, 0, 0, 0]

def menu():
    print("\n=== Draw the Beetle — IA ===")
    print("1 - Executar Expectiminimax")
    print("2 - Executar Expectiminimax com Poda Alfa-Beta")
    print("3 - Visualizar árvore (Expectiminimax)")
    print("4 - Visualizar árvore (Alfa-Beta)")
    print("0 - Sair")
    return input("Escolha: ")

def main():
    while True:
        option = menu()

        if option == "0":
            break

        depth = int(input("Profundidade máxima da árvore: "))
        if option == "1":
            memo = {}
            value = expectiminimax(INITIAL_STATE, 0, depth, memo)
            print("Valor esperado:", value)
        elif option == "2":
            memo = {}
            value = expectiminimax_ab(INITIAL_STATE, 0, depth, float("-inf"), float("inf"), memo)
            print("Valor esperado:", value)
        elif option == "3":
            print_tree(INITIAL_STATE, 0, depth, use_ab=False)
        elif option == "4":
            print_tree(INITIAL_STATE, 0, depth, use_ab=True)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
from beetle_game import BeetleGame
from minimax import expectiminimax
from tree_visualizer import TreeCollector
from heuristics import heuristic


def ask_int(prompt, default=None):
    try:
        v = input(prompt)
        if v.strip()=="" and default is not None:
            return default
        return int(v)
    except:
        return default

def main():
    game = BeetleGame()
    state_max = game.initial_state()
    state_min = game.initial_state()

    show_tree = input("Gerar árvore de busca? (s/n): ").lower()=="s"
    tree = TreeCollector() if show_tree else None

    use_heur = input("Usar heurística? (s/n): ").lower()=="s"
    max_depth = ask_int("Profundidade máxima (0=ilimitado): ", 0)
    if max_depth==0:
        max_depth = None

    eval_fn = heuristic if use_heur else (lambda s:0)

    value, policy = expectiminimax(
        game, state_max, state_min,
        True, tree, depth=0,
        max_depth=max_depth,
        eval_fn=eval_fn
    )

    print("\nResultado final")
    print("Valor esperado:", value)
    print("Política ótima:", policy)

    if tree:
        print("\nÁrvore de busca:")
        tree.print_tree()

if __name__=="__main__":
    main()
from beetle_game import BeetleGame
from minimax import minimax, alphabeta
from tree_visualizer import TreeCollector
from heuristics import heuristic


def ask_int(prompt, default=None):
    try:
        v = input(prompt)
        if v.strip() == "" and default is not None:
            return default
        return int(v)
    except Exception:
        return default


def main():
    game = BeetleGame()
    state_max = game.initial_state()
    state_min = game.initial_state()

    print("Escolha o algoritmo:")
    print("1 - MiniMax")
    print("2 - MiniMax com Poda Alfa-Beta")
    algo = ask_int("> ", 1)

    show_tree = input("Gerar árvore de busca? (s/n): ").lower() == "s"
    tree = TreeCollector() if show_tree else None

    use_heur = input("Usar heurística de avaliação? (s/n): ").lower() == "s"

    max_depth = ask_int("Profundidade máxima (0 = ilimitado, recomendável >0): ", 0)
    if max_depth == 0 and not use_heur:
        # garante limite para evitar busca infinita
        max_depth = sum([1, 1, 6, 2, 2, 1])

    eval_fn = heuristic if use_heur else (lambda a, b: 0)

    if algo == 1:
        value, path = minimax(game, state_max, state_min, True, tree,
                              depth=0, max_depth=(None if max_depth == 0 else max_depth), eval_fn=eval_fn)
    else:
        value, path = alphabeta(
            game, state_max, state_min,
            -float("inf"), float("inf"), True, tree,
            depth=0, max_depth=(None if max_depth == 0 else max_depth), eval_fn=eval_fn
        )

    print("\nResultado final:")
    print("Valor:", value)
    # format path with player labels for clarity
    formatted = [f"{p}:{a}" for (p, a) in path]
    print("Caminho solução (ações):", formatted)

    if tree:
        print("\nÁrvore de busca:")
        tree.print_tree()


if __name__ == "__main__":
    main()
import time
import matplotlib.pyplot as plt
import os

from beetle_game import BeetleGame
from minimax import minimax, alphabeta


def run_benchmark():
    game = BeetleGame()
    state_max = game.initial_state()
    state_min = game.initial_state()

    # Profundidades testadas
    depths = list(range(2, 27, 4))

    minimax_times = []
    alphabeta_times = []

    for d in depths:
        print(f"Testando profundidade = {d}")

        # ---------- MiniMax ----------
        # start = time.perf_counter()
        # minimax(
        #     game,
        #     state_max,
        #     state_min,
        #     maximizing=True,
        #     tree=None,
        #     depth=0,
        #     max_depth=d,
        #     eval_fn=lambda a, b: 0  # sem heurística
        # )
        # end = time.perf_counter()
        # minimax_times.append(end - start)

        # ---------- Alfa-Beta ----------
        start = time.perf_counter()
        alphabeta(
            game,
            state_max,
            state_min,
            alpha=-float("inf"),
            beta=float("inf"),
            maximizing=True,
            tree=None,
            depth=0,
            max_depth=d,
            eval_fn=lambda a, b: 0  # sem heurística
        )
        end = time.perf_counter()
        alphabeta_times.append(end - start)

    plot_results(depths, minimax_times, alphabeta_times)


def plot_results(depths, minimax_times, alphabeta_times):
    plt.figure()
    # plt.plot(depths, minimax_times, marker="o", label="MiniMax")
    plt.plot(depths, alphabeta_times, marker="o", label="MiniMax + Alfa-Beta")

    plt.xlabel("Profundidade máxima")
    plt.ylabel("Tempo de execução (segundos)")
    plt.title("Crescimento do tempo com aumento da profundidade")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join("benchmark", "benchmark_depth_2.png"))
    plt.close()


if __name__ == "__main__":
    run_benchmark()
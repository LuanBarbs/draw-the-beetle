import time
import math
from beetle_game import GameState
from ai import minimax_alpha_beta

def run_simulation(num_games=50, depth_p1=2, depth_p2=4):
    p1_wins = 0
    p2_wins = 0
    total_turns = []

    print(f"Iniciando simulação: {num_games} jogos (P1 Prof: {depth_p1} vs P2 Prof: {depth_p2})")
    
    for i in range(num_games):
        game = GameState()
        turn_count = 0
        
        while True:
            terminou, vencedor = game.is_terminal()
            if terminou:
                if vencedor == 0: p1_wins += 1
                else: p2_wins += 1
                total_turns.append(turn_count)
                break
            
            # P1 usa uma profundidade, P2 usa outra (ou a mesma)
            d = depth_p1 if game.turn == 0 else depth_p2
            _, move = minimax_alpha_beta(game, d, -math.inf, math.inf, True, game.turn)
            
            if move is None: # Empate técnico ou sem jogadas
                break
                
            game = game.apply_move(move)
            turn_count += 1
        
        if (i+1) % 10 == 0:
            print(f"Partida {i+1} concluída...")

    avg_turns = sum(total_turns) / len(total_turns) if total_turns else 0
    
    print("\n--- RESULTADOS DOS EXPERIMENTOS ---")
    print(f"Vitórias P1 (Depth {depth_p1}): {p1_wins} ({(p1_wins/num_games)*100:.1f}%)")
    print(f"Vitórias P2 (Depth {depth_p2}): {p2_wins} ({(p2_wins/num_games)*100:.1f}%)")
    print(f"Média de turnos por partida: {avg_turns:.2f}")

if __name__ == "__main__":
    # Experimento 1: IA Inteligente (4) vs IA Rápida (2)
    run_simulation(num_games=50, depth_p1=2, depth_p2=4)
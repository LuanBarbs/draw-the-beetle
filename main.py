import time
import math
from beetle_game import GameState, NOMES
from ai import minimax_alpha_beta

def get_human_move(state):
    moves = state.get_valid_moves()
    print("\nJogadas Disponíveis:")
    for i, m in enumerate(moves):
        tipo, idx, target = m

        if tipo == 'shield':
            print(f"{i}: Ativar ESCUDO (Proteção por 2 turnos)")
        else:
            acao = "Adicionar" if tipo == 'add' else "REMOVER"
            alvo = "seu besouro" if target == state.turn else "besouro INIMIGO"
            print(f"{i}: {acao} {NOMES[idx]} ({alvo})")

    while True:
        try:
            choice = int(input("Escolha sua jogada (número): "))
            if 0 <= choice < len(moves):
                return moves[choice]
        except ValueError:
            pass
        print("Escolha inválida.")

def play_game(mode):
    # mode: 1 (PvCPU), 2 (CPUvCPU)
    game = GameState()
    depth = 4 # Profundidade da busca (Aumentar deixa mais inteligente e lento)

    print("\n--- INÍCIO DO JOGO ---")
    game.print_board()

    while True:
        terminou, vencedor = game.is_terminal()
        if terminou:
            print(f"\nO Jogo Acabou! Vencedor: Jogador {vencedor + 1}")
            break

        current_player = game.turn
        print(f"\n Vez do Jogador {current_player + 1}")

        move = None
        
        # Lógica de Controle
        if mode == 1: # Humano (P1) vs CPU (P2)
            if current_player == 0:
                move = get_human_move(game)
            else:
                print("CPU calculando...")
                _, move = minimax_alpha_beta(game, depth, -math.inf, math.inf, True, current_player)
        
        elif mode == 2: # CPU vs CPU
            print(f"CPU {current_player + 1} pensando...")
            time.sleep(1)
            _, move = minimax_alpha_beta(game, depth, -math.inf, math.inf, True, current_player)

        # Aplicar movimento
        tipo, idx, target = move

        if tipo == 'shield':
            print(f">>> Jogador {current_player+1} ativou um ESCUDO!")
        else:
            desc_acao = "construiu" if tipo == 'add' else "destruiu"
            quem = "o próprio" if target == current_player else "o INIMIGO"
            print(f">>> Jogador {current_player+1} {desc_acao} {NOMES[idx]} em {quem}.")

        game = game.apply_move(move)
        game.print_board()

if __name__ == "__main__":
    print("Deem boas vindas ao JOGADOR! Que comece a batalha do Besouro!")
    print("1. Humano vs CPU")
    print("2. CPU vs CPU")
    opt = input("Escolha o modo: ")
    
    if opt == '1':
        play_game(1)
    elif opt == '2':
        play_game(2)
    else:
        print("Opção inválida")
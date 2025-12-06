import math
from beetle_game import GameState, LIMITES

PESOS = [10, 8, 2, 3, 3, 2]

def evaluate(state, player_idx):
    """
    Função de Avaliação Heurística.
    Retorna um valor numérico indicando a vantagem do player_idx.
    """
    terminou, vencedor = state.is_terminal()
    if terminou:
        if vencedor == player_idx:
            return 10000 # Vitória certa
        else:
            return -10000 # Derrota certa
        
    my_score = 0
    opp_score = 0
    
    opp_idx = 1 - player_idx

    for i in range(6):
        my_score += state.board[player_idx][i] * PESOS[i]
        opp_score += state.board[opp_idx][i] * PESOS[i]

    return my_score - opp_score

def minimax_alpha_beta(state, depth, alpha, beta, maximizing_player, player_id):
    terminou, _ = state.is_terminal()
    if depth == 0 or terminou:
        return evaluate(state, player_id), None

    valid_moves = state.get_valid_moves()

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for move in valid_moves:
            child_state = state.apply_move(move)
            eval_val, _ = minimax_alpha_beta(child_state, depth - 1, alpha, beta, False, player_id)
            
            if eval_val > max_eval:
                max_eval = eval_val
                best_move = move
            
            alpha = max(alpha, eval_val)
            if beta <= alpha:
                break # Poda Beta
        return max_eval, best_move
    
    else: # Minimizing player (Oponente)
        min_eval = math.inf
        best_move = None
        for move in valid_moves:
            child_state = state.apply_move(move)
            eval_val, _ = minimax_alpha_beta(child_state, depth - 1, alpha, beta, True, player_id)
            
            if eval_val < min_eval:
                min_eval = eval_val
                best_move = move
            
            beta = min(beta, eval_val)
            if beta <= alpha:
                break # Poda Alfa
        return min_eval, best_move
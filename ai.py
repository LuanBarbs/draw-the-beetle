import math
from heuristics import heuristic

def minimax_alpha_beta(state, depth, alpha, beta, maximizing, player_id):
    terminal, winner = state.is_terminal()
    if depth == 0 or terminal:
        if terminal:
            return (10000 if winner == player_id else -10000), None
        return heuristic(state, player_id), None

    moves = state.get_valid_moves()
    if not moves:
        return heuristic(state, player_id), None

    best_move = None

    if maximizing:
        value = -math.inf
        for m in moves:
            child = state.apply_move(m)
            eval_v, _ = minimax_alpha_beta(child, depth-1, alpha, beta, False, player_id)
            if eval_v > value:
                value = eval_v
                best_move = m
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value, best_move
    else:
        value = math.inf
        for m in moves:
            child = state.apply_move(m)
            eval_v, _ = minimax_alpha_beta(child, depth-1, alpha, beta, True, player_id)
            if eval_v < value:
                value = eval_v
                best_move = m
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_move
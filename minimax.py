import math
from copy import deepcopy

try:
    from heuristics import heuristic as default_heuristic
except Exception:
    default_heuristic = None


def minimax(game, state_max, state_min, maximizing, tree=None,
            depth=0, max_depth=None, eval_fn=None):
    if eval_fn is None:
        eval_fn = default_heuristic

    if game.is_terminal(state_max):
        return 1, []
    if game.is_terminal(state_min):
        return -1, []

    if max_depth is not None and depth >= max_depth:
        return (eval_fn(state_max, state_min) if eval_fn else 0), []

    if maximizing:
        best_value = -math.inf
        best_path = []
        actions = game.valid_actions(state_max)
        if not actions:
            return (eval_fn(state_max, state_min) if eval_fn else 0), []

        for action in actions:
            new_state = game.apply_action(state_max, action)
            value, path = minimax(game, new_state, state_min, False, tree,
                                  depth + 1, max_depth, eval_fn)

            if tree:
                tree.add("MAX", deepcopy(new_state), deepcopy(state_min), action, value)

            if value > best_value:
                best_value = value
                best_path = [("MAX", action)] + path

        return best_value, best_path

    else:
        best_value = math.inf
        best_path = []
        actions = game.valid_actions(state_min)
        if not actions:
            return (eval_fn(state_max, state_min) if eval_fn else 0), []

        for action in actions:
            new_state = game.apply_action(state_min, action)
            value, path = minimax(game, state_max, new_state, True, tree,
                                  depth + 1, max_depth, eval_fn)

            if tree:
                tree.add("MIN", deepcopy(state_max), deepcopy(new_state), action, value)

            if value < best_value:
                best_value = value
                best_path = [("MIN", action)] + path

        return best_value, best_path


def alphabeta(game, state_max, state_min, alpha, beta, maximizing, tree=None,
              depth=0, max_depth=None, eval_fn=None):
    if eval_fn is None:
        eval_fn = default_heuristic

    if game.is_terminal(state_max):
        return 1, []
    if game.is_terminal(state_min):
        return -1, []

    if max_depth is not None and depth >= max_depth:
        return (eval_fn(state_max, state_min) if eval_fn else 0), []

    if maximizing:
        best_path = []
        actions = game.valid_actions(state_max)
        if not actions:
            return (eval_fn(state_max, state_min) if eval_fn else 0), []

        for action in actions:
            new_state = game.apply_action(state_max, action)
            value, path = alphabeta(
                game, new_state, state_min, alpha, beta, False, tree,
                depth + 1, max_depth, eval_fn
            )

            if tree:
                tree.add("MAX", deepcopy(new_state), deepcopy(state_min), action, value)

            if value > alpha:
                alpha = value
                best_path = [("MAX", action)] + path

            if alpha >= beta:
                break

        return alpha, best_path

    else:
        best_path = []
        actions = game.valid_actions(state_min)
        if not actions:
            return (eval_fn(state_max, state_min) if eval_fn else 0), []

        for action in actions:
            new_state = game.apply_action(state_min, action)
            value, path = alphabeta(
                game, state_max, new_state, alpha, beta, True, tree,
                depth + 1, max_depth, eval_fn
            )

            if tree:
                tree.add("MIN", deepcopy(state_max), deepcopy(new_state), action, value)

            if value < beta:
                beta = value
                best_path = [("MIN", action)] + path

            if beta <= alpha:
                break

        return beta, best_path

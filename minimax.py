import math
from copy import deepcopy

try:
    from heuristics import heuristic as default_heuristic
except Exception:
    default_heuristic = None

DICE_OUTCOMES = [0,1,2,3,4,5]
PROB = 1.0/6.0

def expectiminimax(game, state_max, state_min, maximizing,
                   tree=None, depth=0, max_depth=None, eval_fn=None):

    if eval_fn is None:
        eval_fn = default_heuristic

    if game.is_terminal(state_max):
        return 1.0, []
    if game.is_terminal(state_min):
        return -1.0, []

    if max_depth is not None and depth >= max_depth:
        return (eval_fn(state_max) - eval_fn(state_min)), []

    if maximizing:
        best_value = -math.inf
        best_action = None
        best_path = []

        for action in game.valid_actions(state_max):
            expected_value, _ = chance_node(
                game, state_max, state_min,
                action, True,
                tree, depth, max_depth, eval_fn
            )

            if expected_value > best_value:
                best_value = expected_value
                best_action = action

        return best_value, [("MAX", best_action)]
    else:
        best_value = math.inf
        best_action = None
        best_path = []

        for action in game.valid_actions(state_min):
            expected_value, _ = chance_node(
                game, state_max, state_min,
                action, False,
                tree, depth, max_depth, eval_fn
            )

            if expected_value < best_value:
                best_value = expected_value
                best_action = action

        return best_value, [("MIN", best_action)]

def chance_node(game, state_max, state_min, action, maximizing,
                tree, depth, max_depth, eval_fn):
    expected_value = 0.0

    for outcome in DICE_OUTCOMES:
        new_max = state_max
        new_min = state_min

        if outcome == action:
            if maximizing:
                new_max = game.apply_action(state_max, action)
            else:
                new_min = game.apply_action(state_min, action)

        value, _ = expectiminimax(
            game,
            new_max, new_min,
            not maximizing,
            tree,
            depth+1, max_depth,
            eval_fn
        )

        expected_value += PROB * value

        if tree:
            tree.add(
                "CHANCE", deepcopy(new_max), deepcopy(new_min),
                outcome, value
            )

    return expected_value, []
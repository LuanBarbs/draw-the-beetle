from beetle_game import is_terminal, apply_roll
from heuristics import heuristic

def expectiminimax(state, depth, max_depth, memo):
    state_key = (tuple(state), depth)
    if state_key in memo:
        return memo[state_key]

    if is_terminal(state) or depth == max_depth:
        value = heuristic(state)
        memo[state_key] = value
        return value

    expected_value = 0.0
    for roll in range(1, 7):
        next_state = apply_roll(state, roll)
        value = expectiminimax(next_state, depth + 1, max_depth, memo)
        expected_value += value / 6.0

    memo[state_key] = expected_value
    return expected_value

def expectiminimax_ab(state, depth, max_depth, alpha, beta, memo_ab):
    state_key = (tuple(state), depth)
    if state_key in memo_ab:
        return memo_ab[state_key]

    if is_terminal(state) or depth == max_depth:
        value = heuristic(state)
        memo_ab[state_key] = value
        return value

    value = 0.0
    for roll in range(1, 7):
        next_state = apply_roll(state, roll)
        child_value = expectiminimax_ab(
            next_state, depth + 1, max_depth, alpha, beta, memo_ab
        )
        value += child_value / 6.0

        if value >= beta:
            break
        alpha = max(alpha, value)

    memo_ab[state_key] = value
    return value
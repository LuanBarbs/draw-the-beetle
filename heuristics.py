PESOS = [12, 10, 2, 3, 3, 2]

def heuristic(state, player):
    opp = 1 - player
    score = 0

    for i in range(6):
        score += PESOS[i] * (state.board[player][i] - state.board[opp][i])

    score += 2 * (state.shields[player] - state.shields[opp])
    score += 1 * (state.shield_timer[player] - state.shield_timer[opp])

    return score
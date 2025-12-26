# Heurística baseada em progressão estrutural
# Inspirada em Pearl (1984)

WEIGHTS = [5, 4, 1, 2, 2, 3]

def heuristic(state):
    score = 0
    for i in range(6):
        score += WEIGHTS[i] * state[i] / max(1, WEIGHTS[i])
    return score